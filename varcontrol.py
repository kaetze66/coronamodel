# this is a script that helps keep track of the variables in the model

import pandas as pd
from pathlib import Path
from pysd.py_backend.functions import Model

# Time list is fix and won't change
time_lst = ['INITIAL TIME', 'FINAL TIME', 'SAVEPER']

#init list needs to be updated and copied into the the model.py script
init_lst = ['init Critical Cases', 'init Diseased',
            'init Infected asymptomatic', 'init Infected symptomatic',
            'init Isolated', 'init Recovered', 'init Susceptible',
            'init available test kits', 'init accumulated cases'
            ]
#model list needs to be updated and copied into the the model.py script
model_lst = ['asymptomatic duration', 'contacts per person normal', 'contacts per person symptomatic',
             'duration of treatment', 'fraction of asymptomatic case development', 'fraction of critical cases',
             'fraction of death', 'immunity time', 'infectivity per contact', 'isolation duration',
             'isolation effectiveness', 'symptomatic duration', 'test fraction']

#stock list needs to be updated and copied into the the model.py script
#stocks are sinks that accumulate over time
stock_lst = ['"Infected (asymptomatic)"', '"Infected (symptomatic)"', 'Critical Cases', 'Diseased',
             'Susceptible', 'Isolated', 'Recovered', 'total infected', 'accumulated cases']

#flow list needs to be updated and copied into the the model.py script
#flows are the rates at which persons flow between the stocks
flow_lst = ['critical cases recovery rate', 'death rate', 'deimmunization rate',
            'infected asymptomatic recovery rate', 'infected critical case rate',
            'infected symptomatic recovery rate',
            'infection rate', 'infection rate asymptomatic',
            'infection rate quarantined', 'infection rate symptomatic',
            'isolated recovery rate', 'isolation rate asymptomatic', 'isolation rate symptomatic',
            'isolated critical case rate', 'symptomatic rate', 'new cases']

#endo list needs to be updated and copied into the the model.py script
endo_lst = ['contact infectivity asymptomatic', 'contact infectivity quarantine', 'contact infectivity symptomatic',
            'fraction of symptomatic', 'non controlled population', 'incidence per 100000', 'case fatality rate']

#ignore params are varaibles that are currently not looked at but are in the model for further work
ignore_param_lst = ['available test kits', 'available test kits for testing asymptomatic',
                    'available test kits for testing symptomatic',
                    'effect of kits availability on effectiveness of testing',
                    'kits per person', 'kits population ratio', 'max kits population ratio',
                    'produced test kits',
                    'production phase1', 'production phase2', 'production phase3',
                    'production start phase1', 'production start phase2', 'production start phase3',
                    'production volume phase1', 'production volume phase2', 'production volume phase3',
                    'testing duration', 'tests for symptomatic', 'used test kits',
                    'init total population']

#policy param variables are handled differently in the script and don't have to be copied
policy_param_lst = ['self quarantine effectiveness', 'self quarantine policy',
                    'self quarantine policy SWITCH', 'self quarantine start',
                    'social distancing effectiveness', 'social distancing policy',
                    'social distancing policy SWITCH', 'social distancing start']

ignore_lst = ['TIME', 'TIME STEP']

def run_varcontrol():
    model = Model('corona_base_hackathon_treated.py')
    var_df = model.run()
    var_lst = var_df.columns.tolist()
    print('Total number of variables:', len(var_lst))

    var_lst = [v for v in var_lst if v not in time_lst]
    var_lst = [v for v in var_lst if v not in init_lst]
    var_lst = [v for v in var_lst if v not in model_lst]
    var_lst = [v for v in var_lst if v not in stock_lst]
    var_lst = [v for v in var_lst if v not in flow_lst]
    var_lst = [v for v in var_lst if v not in endo_lst]
    var_lst = [v for v in var_lst if v not in ignore_param_lst]
    var_lst = [v for v in var_lst if v not in policy_param_lst]
    var_lst = [v for v in var_lst if v not in ignore_lst]

    print('Variables that are not sorted yet:', var_lst)
    print('Number of not sorted variables:', len(var_lst))

if __name__ == '__main__':
    run_varcontrol()




