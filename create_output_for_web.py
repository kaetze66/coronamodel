import model_age as mdl
import pathos.pools as pp
from pathlib import Path
import varcontrol
import time
import pandas as pd


def prepare_jobs(step_size,policy_,output_lst,out_path):
    # WARNING: policy_ is now a dict, not a dataframe
    steps_day = step_size
    # writing the files for different measures and different durations of the measures
    # sd: social distancing, sq: self quarantine, sdq: social distancing AND self quarantine
    # code by Robin Schmid and Leon Zueger
    job_list = []
    for measure_ in ['sd', 'sq', 'sqd']:
        for start_day in range(60, 270+steps_day, steps_day):
            for duration in range(steps_day, 180+steps_day, steps_day):
                end_day = start_day + duration
                if end_day <= 270:
                    if measure_ == 'sd':
                        for group in varcontrol.age_groups:
                            policy_['self quarantine %s' % group]['SWITCH'] = 0
                            policy_['social distancing %s' % group]['SWITCH'] = 1
                            policy_['social distancing %s' % group]['start'] = start_day
                            policy_['social distancing %s' % group]['end'] = end_day
                    elif measure_ == 'sq':
                        for group in varcontrol.age_groups:
                            policy_['self quarantine %s' % group]['SWITCH'] = 1
                            policy_['social distancing %s' % group]['SWITCH'] = 0
                            policy_['self quarantine %s' % group]['start'] = start_day
                            policy_['self quarantine %s' % group]['end'] = end_day
                    else:
                        for group in varcontrol.age_groups:
                            policy_['self quarantine %s' % group]['SWITCH'] = 1
                            policy_['social distancing %s' % group]['SWITCH'] = 1
                            policy_['social distancing %s' % group]['start'] = start_day
                            policy_['social distancing %s' % group]['end'] = end_day
                            policy_['self quarantine %s' % group]['start'] = start_day
                            policy_['self quarantine %s' % group]['end'] = end_day

                    pol_df = pd.DataFrame(policy_)
                    pol_df.to_csv(out_path / 'policy_{0}_{1}_{2}.csv'.format(measure_, start_day, end_day))
                    item = (policy_,(measure_,start_day,end_day),output_lst)
                    job_list.append(item)
    print('number of jobs:', len(job_list))
    return job_list

def worker(args):
    from pathlib import Path
    import model_age as mdl
    model = mdl.setup_model()[0]
    results_out_path = Path.cwd() / 'full_results_output'
    pol_out = mdl.run_policy(model,args[0],args[2])
    pol_out.to_csv(results_out_path / 'results_{0}_{1}_{2}.csv'.format(args[1][0], args[1][1], args[1][2]), header=False)
    print('Result: {0}_{1}_{2}'.format(args[1][0], args[1][1], args[1][2]))

if __name__ == '__main__':
    results_out_path = Path.cwd() / 'full_results_output'
    full_out_path = Path.cwd() / 'full_output'
    mdl.clean_output(results_out_path)
    mdl.clean_output(full_out_path)
    start = time.time()
    model = mdl.setup_model()[0]
    output_lst = ['Infected asymptomatic', 'Infected symptomatic', 'Critical Cases', 'Diseased', 'Susceptible','Isolated','Recovered']
    base_df = mdl.run_base(model,output_lst)
    base_df.to_csv(results_out_path / 'base.csv',header=False)
    policy_df = mdl.read_policy()
    pol_params = mdl.set_policy(policy_df)
    job_list = prepare_jobs(10,pol_params,output_lst,full_out_path)
    pool = pp.ProcessPool(nodes=5)
    pool.map(worker,[job for job in job_list])
    pool.close()
    end = time.time()
    print('Total runtime:', end-start)





