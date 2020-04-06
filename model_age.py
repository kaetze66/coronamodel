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
import time
import numpy as np


path = Path.cwd()
out_path = path / 'output'
set_path = path / 'settings'
data_path = path / 'data'

#reading the settings
time_df = pd.read_csv(set_path / 'timesettings.csv',index_col=0)
#init_df = pd.read_csv(set_path / 'initialconditions.csv',index_col=0)
model_df = pd.read_csv(set_path / 'modelsettings.csv',index_col=0)
#contact_df = pd.read_csv(set_path / 'contacts.csv',index_col=0,header=0)
contact_df = pd.read_csv(data_path / 'cm_switzerland_sym.csv',index_col=0)
control_df = pd.read_csv(set_path / 'infectioncontrol.csv',index_col=0)
pop_data = pd.read_csv(data_path / 'pop_data.csv',index_col=0)


# creating the various lists for use later
time_lst = varcontrol.time_lst
model_lst = varcontrol.agify_model()
#stocks are sinks that accumulate over time
stock_lst = varcontrol.agify_stock()
#flows are the rates at which persons flow between the stocks
flow_lst = varcontrol.agify_flow()
endo_lst = varcontrol.agify_endo()
control_lst = varcontrol.agify_infectioncontrol()

def read_policy():
    policy_df = pd.read_csv(set_path / 'policy.csv', index_col=0, header=[0, 1])
    policy_df = policy_df.loc(axis=1)['Switzerland', :]
    policy_df.columns = policy_df.columns.droplevel(level=0)
    return policy_df

def create_output_lst(stocks,flows,endos):
    output_lst = []
    output_lst.extend(stocks)
    output_lst.extend(flows)
    output_lst.extend(endos)
    output_lst.append('infectivity per contact')
    return output_lst

# contact cat are the columns and rows in the contact matrices


def setup_model():
    #handling the paths and the model
    contact_cat = ['80+', '70 - 79', '60 - 69', '50 - 59', '40 - 49', '30 - 39', '20 - 29', '10 - 19', '<10']
    contact_cat = list(zip(varcontrol.age_groups, contact_cat))
    model = Model('corona_hackathon_agegroups_cons_treated.py')

    #updating the time settings
    time_params = {}
    for cond in time_lst:
        time_params[cond] = time_df.loc[cond][0]
    model.set_components(params=time_params)

    # we don't need to read in all initial conditions because they will never change
    # only initial population data is relevant and can be drawn from the data folder
    sum = 0
    init_params = {}
    for group in contact_cat:
        init_params['init Susceptible %s' % group[0]] = pop_data.loc['Switzerland'][group[1]]
        sum += pop_data.loc['Switzerland'][group[1]]
    init_params['init Susceptible'] = sum

    model.set_components(params=init_params)

    #updating the model parameters
    model_params = {}
    for var in model_lst:
        if var[-2:] in varcontrol.age_groups:
            #infectivity per contact is run through all the model as the same variable
            if not var.startswith('infectivity per contact') or var.startswith('contacts per person normal'):
                name, col = var.rsplit(' ',1)
                if col == '00':
                    col = '0'
                model_params[var] = model_df.loc[name][col]
        else:
            model_params[var] = model_df.loc[var]['settings']

    model.set_components(params=model_params)

    contact_param = {}

    for group in contact_cat:
        contact_param['contacts per person normal self %s' % group[0]] = contact_df.loc[group[1]][group[1]]

    # error is here, need to fix
    for src in contact_cat:
        for dst in contact_cat:
            if int(src[0]) < int(dst[0]):
                contact_param['contacts per person normal %sx%s' % (src[0],dst[0])] = contact_df.loc[src[1]][dst[1]]

    model.set_components(params=contact_param)

    control_param = {}
    for group in varcontrol.age_groups:
        control_param['infection start %s' % group] = control_df.loc['infection start %s' % group]['Switzerland']

    model.set_components(params=control_param)

    #making sure all policy switches are set to 0
    pol_switches = {}
    for group in varcontrol.age_groups:
        pol_switches['self quarantine policy SWITCH self %s' % group] = 0
        pol_switches['social distancing policy SWITCH self %s' % group] = 0

    model.set_components(params=pol_switches)

    if set_path.joinpath('calibration.csv').exists():
        calib_dict = {}
        calib_df = pd.read_csv(set_path.joinpath('calibration.csv'),index_col=0)
        for i,row in calib_df.iterrows():
            calib_dict[row.name] = row['calib settings']
        model.set_components(params=calib_dict)

    return model,time_params,contact_cat

def clean_output(out_path):
    try:
        file_lst = list(out_path.glob('*'))
        for file in file_lst:
            file.unlink()
    except FileNotFoundError:
        pass
    out_path.mkdir(exist_ok=True)

def run_base(model,output_lst):
    base_df = model.run(return_columns=output_lst)
    base_df.to_csv(out_path / '00_base_results.csv')
    return base_df

def set_policy(policy_df):

    # current policies available are: self quarantine, social distancing


    pol_params = {}
    for group in varcontrol.age_groups:
        pol_params['self quarantine policy SWITCH self %s' % group] = policy_df.loc['self quarantine %s' % group]['SWITCH']
        pol_params['self quarantine start %s' % group] = policy_df.loc['self quarantine %s' % group]['start']
        pol_params['self quarantine end %s' % group] = policy_df.loc['self quarantine %s' % group]['end']
        pol_params['self quarantine effectiveness %s' % group] = policy_df.loc['self quarantine %s' % group]['effectiveness']
        pol_params['social distancing policy SWITCH self %s' % group] = policy_df.loc['social distancing %s' % group][
            'SWITCH']
        pol_params['social distancing start %s' % group] = policy_df.loc['social distancing %s' % group]['start']
        pol_params['social distancing end %s' % group] = policy_df.loc['social distancing %s' % group]['end']
        pol_params['social distancing effectiveness %s' % group] = policy_df.loc['social distancing %s' % group][
            'effectiveness']
    return pol_params

def run_policy(model,pol_params,output_lst):
    # here we need to just have one input for the multprocessing
    pol_df = model.run(params=pol_params,return_columns=output_lst)
    return pol_df

def combine_runs(base,policy):
    out_df = pd.concat([base,policy],axis=1,keys=['base','policy'])
    out_df.to_csv(out_path / '00_full_results.csv')
    return out_df

def create_output(out_df,time_params,contact_cat,create_graphs):

    cfr_lst = []
    for group in varcontrol.age_groups:
        cfr_lst.append('case fatality rate %s' % group)

    if create_graphs:
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

    cfr_df = pd.read_csv(data_path / 'cfr_age.csv',index_col=0)
    cfr_dict = {}

    index = np.arange(0,time_params['FINAL TIME']+1,1)
    for group in contact_cat:
        dct = {'index':index}
        df = pd.DataFrame(dct)
        df = df.set_index('index',drop=True)
        df['South Korea'] = cfr_df.loc[group[1]]['South Korea']
        df['Spain'] = cfr_df.loc[group[1]]['Spain']
        df['China'] = cfr_df.loc[group[1]]['China']
        df['Italy'] = cfr_df.loc[group[1]]['Italy']
        cfr_dict['case fatality rate %s' % group[0]] = df

    for cfr in cfr_lst:
        df = out_df.loc(axis=1)[:, cfr]
        df.columns = df.columns.droplevel(level=1)
        df = pd.concat([df,cfr_dict[cfr]],axis=1)
        ax = df.plot(title=cfr, legend=True)
        ax.set_xlabel('day')
        ax.set_ylabel('%')
        plt.savefig(out_path.joinpath('01_%s.png' % cfr.replace('"', '')))
        plt.close()

if __name__ == '__main__':
    output_lst = create_output_lst(stock_lst,flow_lst,endo_lst)
    start = time.time()
    clean_output(out_path)
    model,time_params,contact_cat = setup_model()
    base = run_base(model,output_lst)
    policy_df = read_policy()
    pol_params = set_policy(policy_df)
    policy = run_policy(model,pol_params,output_lst)
    out_df = combine_runs(base,policy)
    create_output(out_df,time_params,contact_cat,create_graphs=True)
    end = time.time()
    print('execution time:', end-start)





