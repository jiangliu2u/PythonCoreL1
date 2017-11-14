import threading
from time import sleep, ctime

loops = [10, 4]


class ThreadFunc(object):
    def __init__(self, func, args, name):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop' + str(nloop) + ' at: ' + str(ctime()))
    sleep(nsec)
    print('loop' + str(nloop) + ' done at: ' + str(ctime()))


def main():
    print('starting at: ' + str(ctime()))
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:  # start threads
        threads[i].start()

    for i in nloops:  # wait for all
        threads[i].join()  # threads to finish


if __name__ == '__main__':
    main()
