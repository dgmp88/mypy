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

    def __str__(self):
        return '%1.2f' % self.get_current()

    def get_reset(self):
        t = self.get_current() 
        self.reset()
        return t

    def get_current(self):
        return (time.time()-self.t)*1000


if __name__ == '__main__':
    t = Timer()
    time.sleep(1)
    print(t)
