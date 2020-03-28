import sys
import os

#handling the paths and the model
cwd = os.getcwd()
sys.path.append(cwd)

from pathlib import Path
from pysd.py_backend.functions import Model
import matplotlib.pyplot as plt
import pandas as pd
import varcontrol

#handling the paths and the model
model = Model('corona_base_hackathon_agegroups_treated.py')
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
contact_df = pd.read_csv(set_path / 'contacts.csv',index_col=0,header=0)

time_lst = varcontrol.time_lst

init_lst = varcontrol.agify_init()

model_lst = varcontrol.agify_model()

#stocks are sinks that accumulate over time
stock_lst = varcontrol.agify_stock()
#flows are the rates at which persons flow between the stocks
flow_lst = varcontrol.agify_flow()

endo_lst = varcontrol.agify_endo()

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
    if cond[-2:] in varcontrol.age_groups:
        name, col = cond.rsplit(' ',1)
        init_params[cond] = init_df.loc[name][col]
    else:
        init_params[cond] = init_df.loc[cond][0]
model.set_components(params=init_params)

#updating the model parameters
model_params = {}
for var in model_lst:
    if var[-2:] in varcontrol.age_groups:
        #infectivity per contact is run through all the model as the same variable
        if not var.startswith('infectivity per contact') or var.startswith('contacts per person normal'):
            name, col = var.rsplit(' ',1)
            model_params[var] = model_df.loc[name][col]
    else:
        model_params[var] = model_df.loc[var]['settings']

model.set_components(params=model_params)

contact_param = {}

contact_param['contacts per person normal self 80'] = contact_df.loc['80+']['80+']
contact_param['contacts per person normal self 70'] = contact_df.loc['70 - 79']['70 - 79']
contact_param['contacts per person normal 70x80'] = contact_df.loc['70 - 79']['80+']

model.set_components(params=contact_param)

base_df = model.run(return_columns=output_lst)
base_df.to_csv(out_path / '00_base_results.csv')

# current policies available are: self quarantine, social distancing
pol_dict = {}
#list is SWITCH, start, effectiveness
pol_dict['self quarantine'] = policy_df.loc['self quarantine'].tolist()
pol_dict['social distancing'] = policy_df.loc['social distancing'].tolist()
pol_dict['self quarantine 80'] = policy_df.loc['self quarantine 80'].tolist()
pol_dict['social distancing 80'] = policy_df.loc['social distancing 80'].tolist()
pol_dict['self quarantine 70'] = policy_df.loc['self quarantine 70'].tolist()
pol_dict['social distancing 70'] = policy_df.loc['social distancing 70'].tolist()



pol_params = {'self quarantine policy SWITCH self': pol_dict['self quarantine'][0],
              'self quarantine start': pol_dict['self quarantine'][1],
              'self quarantine effectiveness': pol_dict['self quarantine'][2],
              'social distancing policy SWITCH self': pol_dict['social distancing'][0],
              'social distancing start': pol_dict['social distancing'][1],
              'social distancing effectiveness': pol_dict['social distancing'][2],
              'self quarantine policy SWITCH self 80': pol_dict['self quarantine 80'][0],
              'self quarantine start 80': pol_dict['self quarantine 80'][1],
              'self quarantine effectiveness 80': pol_dict['self quarantine 80'][2],
              'social distancing policy SWITCH self 80': pol_dict['social distancing 80'][0],
              'social distancing start 80': pol_dict['social distancing 80'][1],
              'social distancing effectiveness 80': pol_dict['social distancing 80'][2],
              'self quarantine policy SWITCH self 70': pol_dict['self quarantine 70'][0],
              'self quarantine start 70': pol_dict['self quarantine 70'][1],
              'self quarantine effectiveness 70': pol_dict['self quarantine 70'][2],
              'social distancing policy SWITCH self 70': pol_dict['social distancing 70'][0],
              'social distancing start 70': pol_dict['social distancing 70'][1],
              'social distancing effectiveness 70': pol_dict['social distancing 70'][2],
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





