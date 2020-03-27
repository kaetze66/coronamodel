import pysd
from pathlib import Path
from pysd.py_backend.functions import Model
import matplotlib.pyplot as plt
import pandas as pd

#handling the paths and the model
path = Path.cwd()
model = Model('corona_base_v2_treated.py')
out_path = path / 'output'
set_path = path / 'settings'
out_path.mkdir(exist_ok=True)

#reading the settings
policy_df = pd.read_csv(set_path / 'policy.csv',index_col=0)
time_df = pd.read_csv(set_path / 'timesettings.csv',index_col=0)

time_params = {'INITIAL TIME': time_df.loc['INITIAL TIME'][0],'FINAL TIME': time_df.loc['FINAL TIME'][0], 'SAVEPER': time_df.loc['SAVEPER'][0]}

model.set_components(params=time_params)

# current policies available are: self quarantine, social distancing

pol_dict = {}
#list is SWITCH, start, effectiveness
pol_dict['self quarantine'] = policy_df.loc['self quarantine'].tolist()
pol_dict['social distancing'] = policy_df.loc['social distancing'].tolist()

base_df = model.run()
base_df.to_csv(out_path / '00_base_results.csv')

pol_params = {'self quarantine policy SWITCH': pol_dict['self quarantine'][0],
              'self quarantine start': pol_dict['self quarantine'][1],
              'self quarantine effectiveness': pol_dict['self quarantine'][2],
              'social distancing policy SWITCH': pol_dict['social distancing'][0],
              'social distancing start': pol_dict['social distancing'][1],
              'social distancing effectiveness': pol_dict['social distancing'][2],
              }

pol_df = model.run(params=pol_params)
out_df = pd.concat([base_df,pol_df],axis=1,keys=['base','policy'])
out_df.to_csv(out_path / '00_full_results.csv')

#stocks are sinks that accumulate over time
stock_lst = ['"Infected (asymptomatic)"', '"Infected (symptomatic)"', 'Critical Cases', 'Diseased',
             'Susceptible', 'Isolated', 'Recovered', 'total infected']
#flows are the rates at which persons flow between the stocks
flow_lst = ['critical cases recovery rate', 'death rate', 'deimmunization rate',
            'infected asymptomatic recovery rate', 'infected critical case rate',
            'infected symptomatic recovery rate',
            'infection rate', 'infection rate asymptomatic',
            'infection rate quarantined', 'infection rate symptomatic',
            'isolated recovery rate', 'isolation rate asymptomatic', 'isolation rate symptomatic',
            'isolated critical case rate', 'symptomatic rate']

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

