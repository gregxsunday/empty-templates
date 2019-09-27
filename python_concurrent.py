from concurrent.futures import ThreadPoolExecutor as PoolExecutor
#from concurrent.futures import ProcessPoolExecutor as PoolExecutor

def func():
    pass

if __name__ == '__main__':
    payloads = []
    with PoolExecutor(max_workers=10) as executor:
        for _ in executor.map(func, payloads):
            pass