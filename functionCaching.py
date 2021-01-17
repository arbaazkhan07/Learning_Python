import time
from functools import lru_cache


@lru_cache(maxsize=10)
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print('now running some work')
    some_work(2)
    print('Done... Calling again...')
    some_work(2)
    print('Called again...')
