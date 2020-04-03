import sys
import os

#handling the paths and the model
cwd = os.getcwd()
sys.path.append(cwd)

from pathlib import Path
from pysd.py_backend.functions import Model
import pandas as pd
import varcontrol
import time



#handling the paths and the model
def run_model_web(switch0=0,start0=0,end0=0,effectiveness0=0,switch1=0,start1=0,end1=0,effectiveness1=0,switch2=0,start2=0,end2=0,effectiveness2=0,switch3=0,start3=0,end3=0,effectiveness3=0,
                  switch4=0,start4=0,end4=0,effectiveness4=0,switch5=0,start5=0,end5=0,effectiveness5=0,switch6=0,start6=0,end6=0,effectiveness6=0,switch7=0,start7=0,end7=0,effectiveness7=0,
                  switch8=0,start8=0,end8=0,effectiveness8=0,switch9=0,start9=0,end9=0,effectiveness9=0,switch10=0,start10=0,end10=0,effectiveness10=0,switch11=0,start11=0,end11=0,effectiveness11=0,
                  switch12=0,start12=0,end12=0,effectiveness12=0,switch13=0,start13=0,end13=0,effectiveness13=0,switch14=0,start14=0,end14=0,effectiveness14=0,switch15=0,start15=0,end15=0,effectiveness15=0,
                  switch16=0,start16=0,end16=0,effectiveness16=0,switch17=0,start17=0,end17=0,effectiveness17=0):

    #for the args:
    # there are a total of 18 sets of 4 (2 policies times 9 age groups)
    # the first 9 sets are social distancing for the age groups in ascending order, then 9 sets for self quarantine in ascending order

    full_args = [switch0,start0,end0,effectiveness0,switch1,start1,end1,effectiveness1,switch2,start2,end2,effectiveness2,switch3,start3,end3,effectiveness3,
                  switch4,start4,end4,effectiveness4,switch5,start5,end5,effectiveness5,switch6,start6,end6,effectiveness6,switch7,start7,end7,effectiveness7,
                  switch8,start8,end8,effectiveness8,switch9,start9,end9,effectiveness9,switch10,start10,end10,effectiveness10,switch11,start11,end11,effectiveness11,
                  switch12,start12,end12,effectiveness12,switch13,start13,end13,effectiveness13,switch14,start14,end14,effectiveness14,switch15,start15,end15,effectiveness15,
                 switch16,start16,end16,effectiveness16,switch17,start17,end17,effectiveness17]

    pol_dict = {}
    pol_dict['social distancing 00'] = full_args[:4]
    pol_dict['social distancing 10'] = full_args[4:8]
    pol_dict['social distancing 20'] = full_args[8:12]
    pol_dict['social distancing 30'] = full_args[12:16]
    pol_dict['social distancing 40'] = full_args[16:20]
    pol_dict['social distancing 50'] = full_args[20:24]
    pol_dict['social distancing 60'] = full_args[24:28]
    pol_dict['social distancing 70'] = full_args[28:32]
    pol_dict['social distancing 80'] = full_args[32:36]
    pol_dict['self quarantine 00'] = full_args[36:40]
    pol_dict['self quarantine 10'] = full_args[40:44]
    pol_dict['self quarantine 20'] = full_args[44:48]
    pol_dict['self quarantine 30'] = full_args[48:52]
    pol_dict['self quarantine 40'] = full_args[52:56]
    pol_dict['self quarantine 50'] = full_args[56:60]
    pol_dict['self quarantine 60'] = full_args[60:64]
    pol_dict['self quarantine 70'] = full_args[64:68]
    pol_dict['self quarantine 80'] = full_args[68:]



    start = time.time()
    model = Model('corona_hackathon_agegroups_cons_treated.py')
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
    time_df = pd.read_csv(set_path / 'timesettings.csv',index_col=0)
    init_df = pd.read_csv(set_path / 'initialconditions.csv',index_col=0)
    model_df = pd.read_csv(set_path / 'modelsettings.csv',index_col=0)
    contact_df = pd.read_csv(set_path / 'contacts.csv',index_col=0,header=0)
    control_df = pd.read_csv(set_path / 'infectioncontrol.csv',index_col=0)

    time_lst = varcontrol.time_lst

    init_lst = varcontrol.agify_init()

    model_lst = varcontrol.agify_model()

    output_lst = ['Susceptible', 'total infected', 'Critical Cases', 'Diseased']
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
            if col == '00':
                col = '0'
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
                if col == '00':
                    col = '0'
                model_params[var] = model_df.loc[name][col]
        else:
            model_params[var] = model_df.loc[var]['settings']

    model.set_components(params=model_params)

    contact_param = {}

    contact_cat = ['80+', '70 - 79', '60 - 69', '50 - 59', '40 - 49', '30 - 39', '20 - 29', '10 - 19', '<10']
    for i, group in enumerate(varcontrol.age_groups):
        contact_param['contacts per person normal self %s' % group] = contact_df.loc[contact_cat[i]][contact_cat[i]]

    for i, src in enumerate(varcontrol.age_groups):
        for j, dst in enumerate(varcontrol.age_groups):
            if int(src) < int(dst):
                contact_param['contacts per person normal %sx%s' % (src,dst)] = contact_df.loc[contact_cat[i]][contact_cat[j]]

    model.set_components(params=contact_param)

    control_param = {}
    for group in varcontrol.age_groups:
        control_param['infection start %s' % group] = control_df.loc['infection start %s' % group]['settings']

    model.set_components(params=control_param)

    base_df = model.run(return_columns=output_lst)
    #base_df.to_csv(out_path / '00_base_results.csv')

    pol_params = {}
    for group in varcontrol.age_groups:
        pol_params['self quarantine policy SWITCH self %s' % group] = pol_dict['self quarantine %s' % group][0]
        pol_params['self quarantine start %s' % group] = pol_dict['self quarantine %s' % group][1]
        pol_params['self quarantine end %s' % group] = pol_dict['self quarantine %s' % group][2]
        pol_params['self quarantine effectiveness %s' % group] = pol_dict['self quarantine %s' % group][3]
        pol_params['social distancing policy SWITCH self %s' % group] = pol_dict['social distancing %s' % group][0]
        pol_params['social distancing start %s' % group] = pol_dict['social distancing %s' % group][1]
        pol_params['social distancing end %s' % group] = pol_dict['social distancing %s' % group][2]
        pol_params['social distancing effectiveness %s' % group] = pol_dict['social distancing %s' % group][3]

    pol_df = model.run(params=pol_params,return_columns=output_lst)
    out_df = pd.concat([base_df,pol_df],axis=1,keys=['base','policy'])
    out_df.to_csv(out_path / '00_full_results.csv')

    end = time.time()

    print('execution time:', end-start)

if __name__ == '__main__':
    run_model_web()




