# spices - dog , cat
# age <2 and >5

pet = "dog"
age = 4


if pet=="dog" and age <2:
    food = "puppy food"
elif pet == "dog" and age>2:
    food = "senior puppy food"
    
if pet =="cat" and age >5:
    food = "senior cat food"
elif pet =="cat" and age<5:
    food = "junior cat food"

print("food : ",food)