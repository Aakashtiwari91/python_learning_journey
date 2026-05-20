# function with *args(variable arguments )

sum = 0
def add(*args):
    for i in len(*args):
        sum = sum+args
    return sum

print(add(2,3,4,5,67))