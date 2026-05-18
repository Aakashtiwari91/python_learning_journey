# question 1  Age group categrazation
# if <13 = child 13 - 19 = teenager 20-59 = adult 60+ senoir

age = int(input("enter your age"))
if age<13:
    print("child")
elif age >=13 and age <=19:
    print("teenager")
elif age>=20 and age<=59:
    print("adult")
else:
    print("senoir")