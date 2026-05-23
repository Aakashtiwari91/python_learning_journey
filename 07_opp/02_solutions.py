# get method

# class Student:
    
#     def __init__(self,name,age,place,marks):
#         self.__name = name
#         self.age = age
#         self.place = place
#         self.__marks = marks
        
#     def get_name(self):
#         return self.__name
    
#     def set_marks(self):
#         if self.__marks<=0:
#             self.__marks = 33
#             return self.__marks
#         else:
#             return self.__marks

# s = Student("aakash",22,"rewa",21)
# print(s.get_name())
# print(s.age)
# print(s.place)
# print(s.set_marks())



#inheritance

class Car:
    def __init__(self,brand,model,version,category):
        self.brand = brand
        self.model = model
        self.version = version
        self.category = category

class CarColor(Car):
    
    def __init__(self,brand ,model ,version , category,color):
        super().__init__(brand,model , version ,category)
        self.color= color
        
        
class CarCountry(CarColor):
    
    def __init__(self,brand,model , version , category,color,country):
        super().__init__(brand, model ,version, category,color)
        self.country= country
        
# c = Car("bmw","m5cs","bs8","sport")
# c1 = CarColor("bmw","m5cs","bs8","sport","red")
# print(c1.brand)
# print(c1.color)

c2 = CarCountry("bmw","m8cs","v12","supercar","black","india")
print(c2.brand)