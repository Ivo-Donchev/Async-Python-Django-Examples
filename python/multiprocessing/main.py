from sys import argv
import multiprocessing


def cpu_heavy_operation():
    """
    A dummy loop to simulate heavy CPU usage
    """

    for i in range(100000000):
        pass


def main(*, subprocesses_count):
    processes = []

    print(f'Running {subprocesses_count} processes...')

    for i in range(int(subprocesses_count)):
        process = multiprocessing.Process(target=cpu_heavy_operation)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print('Done!')


if __name__ == '__main__':
    if len(argv) != 2:
        print(
            '''
            ERROR:
            You must provide the number of subprocesses!
            Example: `python main.py 3` will use 3 subprocesses
            '''
        )
    else:
        subprocesses_count = argv[1]
        main(subprocesses_count=argv[1])
