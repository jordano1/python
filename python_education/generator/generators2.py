from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        # starts a time
        t1 = time()
        result = fn(*args, **kwargs)  
        t2 = time()  
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5