import model_age as mdl
import pathos.pools as pp
from pathlib import Path
import varcontrol
import time
import pandas as pd
import matplotlib.pyplot as plt


def prepare_jobs(step_size,policy_,output_lst,out_path):
    # WARNING: policy_ is now a dict, not a dataframe
    steps_day = step_size
    initial_time = 90
    # writing the files for different measures and different durations of the measures
    # sd: social distancing, sq: self quarantine, sdq: social distancing AND self quarantine
    # code by Robin Schmid and Leon Zueger
    job_list = []
    for measure_ in ['sd', 'sq', 'sqd']:
        for start_day in range(initial_time, 270+steps_day, steps_day):
            for duration in range(steps_day, 180+steps_day, steps_day):
                end_day = start_day + duration
                if end_day <= 270:
                    if measure_ == 'sd':
                        for group in varcontrol.age_groups:
                            policy_['self quarantine policy SWITCH self %s' % group] = 0
                            policy_['social distancing policy SWITCH self %s' % group] = 1
                            policy_['social distancing start %s' % group] = start_day
                            policy_['social distancing end %s' % group] = end_day
                    elif measure_ == 'sq':
                        for group in varcontrol.age_groups:
                            policy_['self quarantine policy SWITCH self %s' % group] = 1
                            policy_['social distancing policy SWITCH self %s' % group] = 0
                            policy_['self quarantine start %s' % group] = start_day
                            policy_['self quarantine end %s' % group] = end_day
                    else:
                        for group in varcontrol.age_groups:
                            policy_['self quarantine policy SWITCH self %s' % group] = 1
                            policy_['social distancing policy SWITCH self %s' % group] = 1
                            policy_['social distancing start %s' % group] = start_day
                            policy_['social distancing end %s' % group] = end_day
                            policy_['self quarantine start %s' % group] = start_day
                            policy_['self quarantine end %s' % group] = end_day

                    # we should write the policy file into a more readable version
                    # getting the names of the variables could also be hardcoded but if we expand this, this is going to be easier
                    row_names = list(policy_.keys())
                    row_names = [name.rsplit(' ',1)[0] for name in row_names]
                    row_names = list(set(row_names))


                    pol_df = pd.DataFrame(index=row_names,columns=varcontrol.age_groups)
                    for key,val in policy_.items():
                        row,col = key.rsplit(' ',1)
                        pol_df.loc[row][col] = val
                    pol_df.to_csv(out_path / 'policy_{0}_{1}_{2}.csv'.format(measure_, start_day-initial_time, end_day-initial_time))
                    item = (policy_.copy(),(measure_,start_day-initial_time,end_day-initial_time),output_lst)
                    job_list.append(item)
    print('number of jobs:', len(job_list))
    return job_list

def worker(args):
    from pathlib import Path
    import model_age as mdl
    model = mdl.setup_model()[0]
    results_out_path = Path.cwd() / 'full_results_output'
    pol_out = mdl.run_policy(model,args[0],args[2])
    pol_out = pol_out.reset_index(drop=True)
    pol_out.to_csv(results_out_path / 'results_{0}_{1}_{2}.csv'.format(args[1][0], args[1][1], args[1][2]))
    print('Result: {0}_{1}_{2}'.format(args[1][0], args[1][1], args[1][2]))

def check_result(path):
    """
    from pathlib import Path
    results_out_path = Path.cwd() / 'full_results_output'
    import create_output_for_web
    create_output_for_web.check_result(results_out_path)
    """
    file_list = list(path.glob('*'))[:20]
    sum_df = pd.DataFrame()
    for file in file_list:
        df = pd.read_csv(file,index_col=0)
        sum_df = pd.concat([sum_df,df],axis=1)
    
    ax = sum_df.plot(legend=False)
    plt.savefig('test.png')

if __name__ == '__main__':
    results_out_path = Path.cwd() / 'full_results_output'
    full_out_path = Path.cwd() / 'full_output'
    mdl.clean_output(results_out_path)
    mdl.clean_output(full_out_path)
    start = time.time()
    model = mdl.setup_model()[0]
    output_lst = ['Infected asymptomatic', 'Infected symptomatic', 'Critical Cases', 'Diseased', 'Susceptible','Isolated','Recovered']
    base_df = mdl.run_base(model,output_lst)
    base_df = base_df.reset_index(drop=True)
    base_df.to_csv(results_out_path / 'results_base.csv')
    policy_df = mdl.read_policy()
    pol_params = mdl.set_policy(policy_df)
    job_list = prepare_jobs(1,pol_params,output_lst,full_out_path)
    #warning, adjust the processes before you run it on your machine
    pool = pp.ProcessPool(nodes=32)
    prep = time.time()
    print('Preparation time:', prep-start)
    pool.map(worker,[job for job in job_list])
    pool.close()
    end = time.time()
    print('Total runtime:', end-start)
    check_result(results_out_path)





