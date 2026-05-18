# day - sunny - Go for a walk
# day - rainy - Read a book
# day - snowy - build a snowman

day = "sunny"

if day == "sunny":
    activity = "Go for a walk"
elif day == "rainy":
    activity = "Read a book"
elif day == "snowy":
    activity = "build a snowman"
else:
    print("Go to your work , have a nice day")
print(F"your activity : {activity}")