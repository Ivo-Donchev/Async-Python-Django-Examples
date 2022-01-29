from sys import argv
import asyncio
import threading


async def func():
    print("Async")
    await asyncio.sleep(1)
    print(f"Django in thread {threading.currentThread().ident}")


async def main(*, coroutines_count):
    print(f'Running {coroutines_count} coroutines...')
    await asyncio.gather(*[func() for i in range(int(coroutines_count))])
    print('Done!')


if __name__ == '__main__':
    if len(argv) != 2:
        print(
            '''
            ERROR:
            You must provide the number of coroutines!
            Example: `python main.py 3` will use 3 coroutines
            '''
        )
    else:
        coroutines_count = argv[1]
        asyncio.run(main(coroutines_count=argv[1]))
