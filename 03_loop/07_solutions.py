# user_input = int(input("enter a number"))

# while True:
#     if user_input >=1 and user_input <=10:
#         print(F"congratulations your number is right and the number is :",user_input)
#         exit()
#     else:
#         user_input = int(input("enter number again"))



while True:
    number = int(input("enter a valid number between 1 to 10: "))
    if number >=1 and number <=10:
        print("thanks , you got it")
        break;
    else:
        print("invalid number try again")