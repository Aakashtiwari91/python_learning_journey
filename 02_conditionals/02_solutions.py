# question 2  movie ticket pricing
# for adults (18 and over ) - $12
# for child (<18)- $8
# to wednesday - off $2

#method 1
'''
day = str(input("enter week day name: "))
age = int(input("enter your age: "))

if age <18:
    if day =="wednesday":
        print("today you got $2 discount so total ticket price is %6 only")
    else:
        print("ticket price is $8 only")
elif age >=18:
    if day =="wednesday":
        print("today you got $2 discount so total ticket price is $10 only")
    else:
        print("ticket price is $12 only")
        
'''
#method 2

age = int(input("Enter your age : "))
day  = input("Enter today week day name: ")
day_name = day.title()
price = 0

if age <18:
    price = 8
else:
    price = 12

if day_name =="Wednesday":
    price = price-2


print(F"your ticket price is $ {price}")
