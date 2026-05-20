# print N to 1 using recursion

def print_number(n):
    if n==1:
        return 1
    print_number(n-1)
print(print_number(5))