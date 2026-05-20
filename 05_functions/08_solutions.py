
# ** kwargs

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(F"key : {key} and value : {value}")
        
print_kwargs(name="aakash",age=32,place="majhiyaar")