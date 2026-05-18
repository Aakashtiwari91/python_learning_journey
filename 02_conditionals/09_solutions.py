#leep year or not 
# divisible by 4 and not divisible by 100 or divisible by 400

year = int(input("Enter  a year"))

if  (year %4==0 and year %100 !=0) or year%400 ==0:
    print("leap year")
else:
    print("not leap year")