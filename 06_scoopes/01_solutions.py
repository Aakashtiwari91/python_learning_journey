# scoope in python

x = 99

# 3.

# def func3():
#     global x     # over ride global variable
#     x = 12

# func3()
# print(x)


#4.

# def f1():
#     # x = 88
#     def f2():
#         print(x)
#     return f2
# result = f1()
# result()



#5. 
def chaicoder(num):
    def actual(x):
        return x** num
    return actual

result = chaicoder(5)
print(result(3))