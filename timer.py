import time

class Timer():
    '''
    Super simple timer class, useful for profiling stuff - particularly asynchronous stuff where
    line_profiler fails
    '''

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.t = time.time()

    def print(self):
        print('%1.2f' % self.get_current_ms())

    def get_reset(self):
        t = self.get_current() 
        self.reset()
        return t

    def get_current(self):
        return (time.time()-self.t)*1000


