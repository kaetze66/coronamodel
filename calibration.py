# script for calibration to a countries data
# make sure the country data is loaded

from pathlib import Path
import pandas as pd
import scipy.optimize as opt
import model_age
import numpy as np
import matplotlib.pyplot as plt
import time
import varcontrol

class Calibrate:
    def __init__(self):
        input = model_age.setup_model()
        self.model = input[0]
        self.time_params = input[1]
        self.contact_cat = input[2]
        self.data_dict = {}
        self.out_vars = ['Critical Cases', 'Diseased']
        self.return_ts = []
        self.cal_vars = []
        self.cal_bounds = []
        self.data_path = Path.cwd() / 'data'
        self.calib_path = Path.cwd() / 'calib'
        self.base_data_error = 0

    def calibrate(self):
        def error_function(param_list):
            out = self.model.run(params=dict(zip(self.cal_vars,param_list)),return_columns=self.out_vars)
            out = out.loc[self.return_ts]
            error = 0
            for var in self.out_vars:
                error += sum((out[var]-self.data_dict[var])**2)
            error = error / self.base_data_error
            print('Error:', error)
            return error

        # cal vals are the variables that we calibrate
        self.cal_vars = ['infectivity per contact']
        # bounds are the min and max values for the cal vals
        cal_bounds = [(0.001,0.025)]
        guess_list = np.array([0.0125])

        #calculate the base data error for normalizing the error
        base_df = self.model.run(return_columns=self.out_vars)
        base_df = base_df.loc[self.return_ts]
        error = 0
        for var in self.out_vars:
            error += sum((base_df[var] - self.data_dict[var]) ** 2)
        self.base_data_error = error


        res = opt.minimize(error_function,guess_list,bounds=cal_bounds)

        return res.x



    def read_data(self):
        cc_df = pd.read_csv(self.data_path / 'critical_cases_switzerland.csv',index_col=0)
        dis_df = pd.read_csv(self.data_path / 'diseased_switzerland.csv',index_col=0)
        cc_data = cc_df['Switzerland']
        #cc_data.name = 'Critical Cases'
        dis_data = dis_df['Switzerland']
        #dis_data.name = 'Diseased'
        # we need to make sure that all time stamps are in the data
        self.return_ts = list(map(int, dis_data.index))
        self.data_dict['Critical Cases'] = cc_data
        self.data_dict['Diseased'] = dis_data

    def calib_output(self,res):
        self.model.set_components(params=dict(zip(self.cal_vars,res)))
        output_vars = []
        cfr_lst = []
        for group in varcontrol.age_groups:
            cfr_lst.append('case fatality rate %s' % group)
        output_vars.extend(cfr_lst)
        output_vars.extend(self.out_vars)
        out_df = self.model.run(return_columns=output_vars)
        for var in self.out_vars:
            df = pd.concat([out_df[var],self.data_dict[var]],axis=1)
            df = df.loc[self.return_ts]
            ax = df.plot(title=var, legend=True)
            ax.set_xlabel('day')
            ax.set_ylabel('person')
            plt.savefig(self.calib_path.joinpath('calib_%s.png' % var))
            plt.close()

        cfr_df = pd.read_csv(self.data_path / 'cfr_age.csv', index_col=0)
        cfr_dict = {}

        index = np.arange(0, self.time_params['FINAL TIME'] + 1, 1)
        for group in self.contact_cat:
            dct = {'index': index}
            df = pd.DataFrame(dct)
            df = df.set_index('index', drop=True)
            df['South Korea'] = cfr_df.loc[group[1]]['South Korea']
            df['Spain'] = cfr_df.loc[group[1]]['Spain']
            df['China'] = cfr_df.loc[group[1]]['China']
            df['Italy'] = cfr_df.loc[group[1]]['Italy']
            cfr_dict['case fatality rate %s' % group[0]] = df

        cfr_lst = []
        for group in varcontrol.age_groups:
            cfr_lst.append('case fatality rate %s' % group)

        for cfr in cfr_lst:
            print(cfr)
            df = out_df.loc(axis=1)[cfr]
            df = pd.concat([df, cfr_dict[cfr]], axis=1)
            df = df.loc[self.return_ts]
            ax = df.plot(title=cfr, legend=True)
            ax.set_xlabel('day')
            ax.set_ylabel('%')
            plt.savefig(self.calib_path.joinpath('01_%s.png' % cfr.replace('"', '')))
            plt.close()



if __name__ == '__main__':
    start = time.time()
    cal = Calibrate()
    cal.read_data()
    res = cal.calibrate()
    print(res)
    cal.calib_output(res)
    end = time.time()
    print('Total calibration time:', end-start)