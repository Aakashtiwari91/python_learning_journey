# find largest number among three number

a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))

if a>b and a>c:
    print("greater number is a: ",a)
elif b>a and b>c:
    print("greater number is b: ",b)
else:
    print("greater number is c :",c)