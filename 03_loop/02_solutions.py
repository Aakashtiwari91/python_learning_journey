# given number n
# sum of even number


total_numbers =int(input("Enter your numbers"))
numbers_list = []
for i in range(0,total_numbers):
    num = int(input("Enter a number : "))
    numbers_list.append(num)

sum_of_even_numbers=0

for num in numbers_list:
    if num%2==0:
        sum_of_even_numbers +=num
print("total sum of even numbers: ",sum_of_even_numbers)