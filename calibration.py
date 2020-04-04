# script for calibration to a countries data
# make sure the country data is loaded

from pathlib import Path
import pandas as pd
p = Path.cwd()
data_path = p / 'data'

def calibrate(model):
    def loss_function(model,param_list):
        out_vars = ['Critical Cases', 'Diseased']
        cc_df = pd.read_csv(data_path / 'critical_cases_switzerland.csv')
        dis_df = pd.read_csv(data_path / 'diseased_switzerland.csv')
        cc_data = cc_df.loc['Switzerland']
        dis_data = dis_df.loc['Switzerland']
        # we need to make sure that all time stamps are in the data
        return_ts = list(map(int,dis_data.index))
        data_dict = {}
        data_dict['Critical Cases'] = cc_data


        # cal vals are the variables that we calibrate
        cal_vars = []

        res = model.run(params=dict(zip(cal_vars,param_list)),return_columns=out_vars,return_ts=return_ts)
        error = 0


        # bounds are the min and max values for the cal vals
        cal_bounds = []