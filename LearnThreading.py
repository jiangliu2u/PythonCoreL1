import threading
from time import ctime, sleep

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop' + str(nloop) + "at" + str(ctime()))
    sleep(nsec)
    print('loop' + str(nloop) + 'done at: ' + str(ctime()))


def main():
    print('starting at: ' + str(ctime()))
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:  # start threads
        threads[i].start()

    for i in nloops:  # wait for all
        threads[i].join()  # threads to finish

    print('all DONE at: ' + str(ctime()))


if __name__ == '__main__':
    main()
