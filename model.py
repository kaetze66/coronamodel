import sys
import os

#handling the paths and the model
cwd = os.getcwd()
sys.path.append(cwd)

import pysd
from pathlib import Path
from pysd.py_backend.functions import Model
import matplotlib.pyplot as plt
import pandas as pd
import varcontrol
import time

start = time.time()

# Set variables to plot stocks and flows
plot_stocks = False
plot_flows = False

model = Model('corona_base_hackathon_treated.py')
path = Path.cwd()
out_path = path / 'output'
set_path = path / 'settings'
full_out_path = path / 'full_output'

try:
    file_lst = list(out_path.glob('*'))
    for file in file_lst:
        file.unlink()
except FileNotFoundError:
    pass
out_path.mkdir(exist_ok=True)

# Changing different parameters
policy_ = pd.read_csv(set_path / 'policy.csv', index_col=0)
time_df = pd.read_csv(set_path / 'timesettings.csv',index_col=0)
init_df = pd.read_csv(set_path / 'initialconditions.csv',index_col=0)
model_df = pd.read_csv(set_path / 'modelsettings.csv',index_col=0)
control_df = pd.read_csv(set_path / 'infectioncontrol.csv',index_col=0)

time_lst = varcontrol.time_lst

init_lst = varcontrol.init_lst

model_lst = varcontrol.model_lst

control_lst = varcontrol.infection_control_lst

#stocks are sinks that accumulate over time
stock_lst = varcontrol.stock_lst
#flows are the rates at which persons flow between the stocks
flow_lst = varcontrol.flow_lst

endo_lst = varcontrol.endo_lst

output_lst = []
output_lst.extend(stock_lst)
output_lst.extend(flow_lst)
output_lst.extend(endo_lst)
#updating the time settings

time_params = {}
for cond in time_lst:
    time_params[cond] = time_df.loc[cond][0]
model.set_components(params=time_params)


#updating the initial conditions
init_params = {}
for cond in init_lst:
    init_params[cond] = init_df.loc[cond][0]
model.set_components(params=init_params)

#updating the model parameters
model_params = {}
for var in model_lst:
    model_params[var] = model_df.loc[var]['settings']
model.set_components(params=model_params)

control_params = {}
for var in control_lst:
    control_params[var] = control_df.loc[var]['settings']
model.set_components(params=control_params)

steps_day = 10
# writing the files for different measures and different durations of the measures
# sd: social distancing, sq: self quarantine, sdq: social distancing AND self quarantine
for measure_ in ['sd', 'sq', 'sqd']:
    for start_day in range(0, 60+steps_day, steps_day):
        for duration in range(steps_day, 90+steps_day, steps_day):
            end_day = start_day + duration
            if measure_ == 'sd':
                policy_.loc['social distancing', 'start'] = start_day
                policy_.loc['social distancing', 'end'] = end_day
                policy_.loc['social distancing', 'SWITCH'] = 1
                policy_.loc['self quarantine', 'SWITCH'] = 0
            elif measure_ == 'sq':
                policy_.loc['self quarantine', 'start'] = start_day
                policy_.loc['self quarantine', 'end'] = end_day
                policy_.loc['self quarantine', 'SWITCH'] = 1
                policy_.loc['social distancing', 'SWITCH'] = 0
            else:
                policy_.loc['self quarantine', 'start'] = start_day
                policy_.loc['self quarantine', 'end'] = end_day
                policy_.loc['social distancing', 'start'] = start_day
                policy_.loc['social distancing', 'end'] = end_day
                policy_.loc['self quarantine', 'SWITCH'] = 1
                policy_.loc['social distancing', 'SWITCH'] = 1

            policy_.to_csv(full_out_path / 'policy_{0}_{1}_{2}'.format(measure_, start_day, end_day))

            #reading the settings
            policy_df = policy_
            #policy_df = pd.read_csv(set_path / 'policy_{0}_{1}_{2}.csv'.format(measure_,start_day, end_day),index_col=0)

            # current policies available are: self quarantine, social distancing
            pol_dict = {}
            # list is SWITCH, start, effectiveness
            pol_dict['self quarantine'] = policy_df.loc['self quarantine'].tolist()
            pol_dict['social distancing'] = policy_df.loc['social distancing'].tolist()

            base_df = model.run(return_columns=output_lst)
            base_df.to_csv(out_path / 'results_base.csv')

            pol_params = {'self quarantine policy SWITCH self': pol_dict['self quarantine'][0],
                          'self quarantine start': pol_dict['self quarantine'][1],
                          'self quarantine end': pol_dict['self quarantine'][2],
                          'self quarantine effectiveness': pol_dict['self quarantine'][3],
                          'social distancing policy SWITCH self': pol_dict['social distancing'][0],
                          'social distancing start': pol_dict['social distancing'][1],
                          'social distancing end': pol_dict['social distancing'][2],
                          'social distancing effectiveness': pol_dict['social distancing'][3],
                          }

            pol_df = model.run(params=pol_params,return_columns=output_lst)
            out_df = pd.concat([base_df,pol_df],axis=1,keys=['base','policy'])
            #out_df = out_df.drop(out_df.index[[0]])
            out_df = out_df.drop(out_df.columns[:36], axis=1)
            out_df = out_df.drop(out_df.columns[9:], axis=1)
            out_df.to_csv(out_path / 'results_{0}_{1}_{2}.csv'.format(measure_, start_day, end_day), header=False)
            print('Result: {0}_{1}_{2}'.format(measure_, start_day, end_day))

            #TODO: plotting very slow in the loop, take outside!
            if plot_stocks:
                for stock in stock_lst:
                    df = out_df.loc(axis=1)[:,stock]
                    df.columns = df.columns.droplevel(level=1)
                    ax = df.plot(title=stock,legend=True)
                    ax.set_xlabel('day')
                    ax.set_ylabel('person')
                    plt.savefig(out_path.joinpath('01_%s.png' % stock.replace('"','')))
                    plt.close()

            if plot_flows:
                for flow in flow_lst:
                    df = out_df.loc(axis=1)[:, flow]
                    df.columns = df.columns.droplevel(level=1)
                    ax = df.plot(title=flow,legend=True)
                    ax.set_xlabel('day')
                    ax.set_ylabel('person/day')
                    plt.savefig(out_path.joinpath('02_%s.png' % flow.replace('"','')))
                    plt.close()

end = time.time()

print('execution time:', end-start)





