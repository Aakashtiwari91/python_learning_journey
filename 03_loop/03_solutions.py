# print table 1 to 10 but skip the 5th iteration

number = 5


for i in range(1,11):
    if i==5:
        continue
    print(i*number)
