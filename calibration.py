# script for calibration to a countries data
# make sure the country data is loaded

def calibrate(model):
    def loss_function(model,param_list):
        # cal vals are the variables that we calibrate
        cal_vals = []
        res = model.run(params=dict(zip(cal_vals,param_list)),return_columns=['infected critical case rate', 'Critical Cases', 'death rate', 'Diseased'])

