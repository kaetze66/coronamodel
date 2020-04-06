import time
import model_age as mdl

def time_setup_model():
    start = time.time()
    model = mdl.setup_model()
    end = time.time()
    print('runtime:', end - start)