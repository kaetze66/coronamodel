import pysd
from pathlib import Path
from pysd.py_backend.functions import Model
import matplotlib.pyplot as plt

path = Path.cwd()
model = Model('corona_base_v2_treated.py')
out_path = path / 'output'
out_path.mkdir(exist_ok=True)
out_df = model.run()
out_df.to_csv(out_path / '00_results.csv')

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
    ax = out_df[stock].plot(title=stock)
    ax.set_xlabel('day')
    ax.set_ylabel('person')
    plt.savefig(out_path.joinpath('01_%s.png' % stock.replace('"','')))
    plt.clf()

for flow in flow_lst:
    ax = out_df[flow].plot(title=flow)
    ax.set_xlabel('day')
    ax.set_ylabel('person/day')
    plt.savefig(out_path.joinpath('02_%s.png' % flow.replace('"','')))
    plt.clf()

