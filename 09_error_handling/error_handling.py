# first way 
file = open("manager.txt",'w')

try:
    file.write("chai aur code")
finally:
    file.close()
    
#second way

with open("manager.txt",'w') as file:
    file.write("chai aur python")