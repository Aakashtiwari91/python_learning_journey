# count positive numbers

numbers = [1,-2,4,5,6,78,-3,-6,6,-2,53983,-8,99,0]
positive_number_count = 0
for nums in numbers:
    if nums>0:
        positive_number_count +=1
print(positive_number_count)