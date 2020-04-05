
import pandas as pd
from pathlib import Path
import numpy as np

p = Path.cwd()
data_path = p / 'data'
contact_cat = ['80+', '70 - 79', '60 - 69', '50 - 59', '40 - 49', '30 - 39', '20 - 29', '10 - 19', '<10']

country_list = ['germany', 'italy', 'finland', 'poland', 'UK', 'netherlands', 'luxembourg', 'belgium']

def cm_sym(file):
    orig_cm = pd.read_csv(data_path / file,index_col=0)
    for i,row in enumerate(contact_cat):
        for j,col in enumerate(contact_cat):
            if i < j:
                value = orig_cm.loc[row][col] + orig_cm.loc[col][row]
                orig_cm.loc[row][col] = value
                orig_cm.loc[col][row] = value
    fname = '%s_sym.csv' % file.replace('.csv','')
    orig_cm.to_csv(data_path / fname)
    
for country in country_list:
    cm_sym('cm_%s.csv' % country)
