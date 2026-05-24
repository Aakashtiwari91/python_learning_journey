import time

def chache(func):
    chache_value = {}
    def wrapper(*args):
        if args in chache_value:
            return chache_value[args]
        result = func(*args)
        chache_value[args]=result
        return result
    return wrapper






@chache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(5,6))