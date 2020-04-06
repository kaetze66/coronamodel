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

model = Model('corona_base_hackathon_treated.py')
path = Path.cwd()
out_path = path / 'output'
set_path = path / 'settings'
try:
    file_lst = list(out_path.glob('*'))
    for file in file_lst:
        file.unlink()
except FileNotFoundError:
    pass
out_path.mkdir(exist_ok=True)

#reading the settings
policy_df = pd.read_csv(set_path / 'policy.csv',index_col=0)
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

# current policies available are: self quarantine, social distancing
pol_dict = {}
#list is SWITCH, start, effectiveness
pol_dict['self quarantine'] = policy_df.loc['self quarantine'].tolist()
pol_dict['social distancing'] = policy_df.loc['social distancing'].tolist()

pol_switches = {}
pol_switches['self quarantine policy SWITCH self'] = 0
pol_switches['social distancing policy SWITCH self'] = 0

model.set_components(params=pol_switches)

base_df = model.run(return_columns=output_lst)
base_df.to_csv(out_path / '00_base_results.csv')

pol_params = {'self quarantine policy SWITCH self': float(pol_dict['self quarantine'][0]),
              'self quarantine start': float(pol_dict['self quarantine'][1]),
              'self quarantine end': float(pol_dict['self quarantine'][2]),
              'self quarantine effectiveness': float(pol_dict['self quarantine'][3]),
              'social distancing policy SWITCH self': float(pol_dict['social distancing'][0]),
              'social distancing start': float(pol_dict['social distancing'][1]),
              'social distancing end': float(pol_dict['social distancing'][2]),
              'social distancing effectiveness': float(pol_dict['social distancing'][3])
              }

pol_df = model.run(params=pol_params,return_columns=output_lst)
out_df = pd.concat([base_df,pol_df],axis=1,keys=['base','policy'])
out_df.to_csv(out_path / '00_full_results.csv')

for stock in stock_lst:
    df = out_df.loc(axis=1)[:,stock]
    df.columns = df.columns.droplevel(level=1)
    ax = df.plot(title=stock,legend=True)
    ax.set_xlabel('day')
    ax.set_ylabel('person')
    plt.savefig(out_path.joinpath('01_%s.png' % stock.replace('"','')))
    plt.close()

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





