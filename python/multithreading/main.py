import time
from sys import argv
import threading


def func():
    time.sleep(1)


def main(*, threads_count):
    threads = []

    print(f'Running {threads_count} threads...')

    for i in range(int(threads_count)):
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('Done!')


if __name__ == '__main__':
    if len(argv) != 2:
        print(
            '''
            ERROR:
            You must provide the number of threads!
            Example: `python main.py 3` will use 3 threads
            '''
        )
    else:
        threads_count = argv[1]
        main(threads_count=argv[1])
