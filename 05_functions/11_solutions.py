# sum of three number

total = 0
def sum_of_three_number(a,b,c):
    total = a+b+c
    return total
# print(sum_of_three_number(2,3,4))


# evn/odd check with multiple parameter

def check_even_odd(a,b):
    if a%2==0 and b%2==0:
        print("both are even")
    elif a%2!=0 and b%2!=0:
        print("both are odd")
    else:
        print("mixed one is even and other one is odd")

# check_even_odd(3,3)


# max of three numbers

def max_number(a,b,c):
    if a>=b and a>=c:
        print("a is max number ",a)
    elif b>=a and b>=c:
        print("b is max number ",b)
    else:
        print("c is max number",c)
# max_number(2,3,4)


#max using *args

def max_find(*args):
    maximum = args[0]
    for i in args:
        if i >maximum:
            maximum = i
    return maximum
# print(max_find(2,3,4,5,6))


# swap two number

def swap_number(a,b):
    print(F"before swapping a is : {a} and b is {b}")
    a = ((a+b)-(b:=a))
    print(F"after swapping a is {a} and b is {b}")

# swap_number(2,3)


#sum using *args

def sum_using_args(*args):
    total_sum = 0
    for i in args:
        total_sum += i
    return total_sum

# print(sum_using_args(1,2,3,4,5,6,7,8,9))


# count even using *args

def count_even(*args):
    count = 0
    for i in args:
        if i%2==0:
            count +=1
    return count
# print(count_even(1,3,4,5,6,7,8,9,10))


# student info print using **kwargs

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(F"key: {key} and value : {value}")
# student_info(name="aakash",age=22,place="majhiyaar")


# *args + **kwargs

def mix_of_args_and_kwargs(*args , **kwargs):
    total_sum = 0
    for i in args:
        total_sum = total_sum+i
    print(total_sum)
    for key , value in kwargs.items():
        print(F"key : {key} and value : {value}")
        

# mix_of_args_and_kwargs(1,2,3,4,5,6,7, name="aakash",age=22)


def mix_version(*args,**kwargs):
    total_sum =0
    total_sum = sum(args)
    return total_sum , kwargs

result = mix_version(1,3,4,5,6,7,fruit="mango",color="yellow",taste="yummmy")
# print(result[0])
# print(result[1])



#multiply all numbers using *args

def multiply(*args):
    total_product = 1
    for i in args:
        total_product = total_product*i
    return total_product

# print(multiply(2,3,4,5))



# factorial using recursion

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

# print(factorial(6))


# find max using recursion

def find_max(arr_list):
    if len(arr_list)==1:
        return arr_list[0]
    
    max_rest = find_max(arr_list[1:])
    
    if arr_list[0]>max_rest:
        return arr_list[0]
    else:
        return max_rest
    
print(find_max([1,3,6,9,3,6]))
        
