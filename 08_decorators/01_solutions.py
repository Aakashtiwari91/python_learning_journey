# decorators

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(F"{func.__name__} ran is {end - end} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    
example_function(2)
