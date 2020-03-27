import pysd
from pathlib import Path
from pysd.py_backend.functions import Model
import matplotlib.pyplot as plt

path = Path.cwd()
model = Model('corona_base_v2_treated.py')
out_df = model.run()
out_df.to_csv('results.csv')
#print(out_df.columns)

#stocks are sinks that accumulate over time
stock_lst = ['"Infected (asymptomatic)"', '"Infected (symptomatic)"', 'Critical Cases', 'Diseased', 'Susceptible', 'Isolated']

for stock in stock_lst:
    ax = out_df[stock].plot(title=stock)
    ax.set_xlabel = 'days'
    ax.set_ylabel = 'person'
    plt.savefig('01_%s.png' % stock.replace('"',''))
    plt.clf()

