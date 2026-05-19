number  = int(input("enter a number"))

i = 2
count = 0
while i <=number/2:
    if number%i==0:
        count =  count+1
    i = i+1
if count ==0:
    print("prime number")
else:
    print("not prime number")
        