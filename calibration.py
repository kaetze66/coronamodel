# script for calibration to a countries data
# make sure the country data is loaded

def calibrate(model):
    def loss_function(model,param_dict):
        res = model.run(params=param_dict,return_columns=[''])
