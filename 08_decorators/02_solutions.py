
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(F"{k} with {v}" for k, v in kwargs.items())
        print(F" calling : {func.__name__} with args {args_value} and {kwargs_value}")
        return func(*args,**kwargs)
    
    return wrapper



@debug
def greet(name , greeting="hello"):
    print(F"{greeting} {name}")
    
greet("aakash",greeting="hanji")