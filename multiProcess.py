from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task  ...pid '.fromat(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task  runs   seconds.'.format(name, (end - start)))

if __name__=='__main__':
    print('Parent process {0}.'.format(os.getpid()))
    p = Pool()
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')