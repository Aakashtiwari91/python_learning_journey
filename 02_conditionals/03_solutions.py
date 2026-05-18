# 90- 100 - A
#80- 89 - B
#70-79 -C
#60-69 -D
#<60 - F

marks = int(input("Enter your marks"))

if marks>100:
    print("Enter a valid marks")
    exit()
if marks >=90:
    Grade = "A"
elif marks >=80:
    Grade = "B"
elif marks >=70:
    Grade ="C"
elif marks >=60:
    Grade = "D"
else:
    Grade = "F"
print(F"your grade is {Grade}")