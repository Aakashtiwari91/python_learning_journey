# <3 - walk
# 3- <15 - bike
# >15 - car

distance = int(input("Enter your distance"))

if distance <3:
    Transport_mode = "walk"
elif distance <15:
    Transport_mode = "bike"
else:
    Transport_mode = "car"
print(F"your should go with {Transport_mode}")