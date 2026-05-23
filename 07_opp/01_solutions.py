# syntax of class

# class Car:
#     brand ="bmw"
#     name ="m5cs"
    
# ob = Car()
# print(ob.brand)
# print(ob.name)






class Car:
    total_car = 0
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1
    
    def get_brand(self):
        return self.__brand + "!"
    
    def combine(self):
        return F"{self.__brand} {self.__model}"
    
    def fuelType(self):
        return "diesel or petrol"
    
    def car_description():
        return "car is means of transport"
    @property
    def model(self):
        return self.__model


# p1 = Car("toyota","corolla")
# print(p1.brand)
# print(p1.model)
# print(p1.combine())



class Electric_car(Car):
    def __init__(self, brand, model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuelType(self):
        return "electric type"


# p2 = Electric_car("tesla","model x","85kwh")

# to check instance(object of the car)

# print(isinstance(p2, Car))
# print(isinstance(p2,Electric_car))



# print(p2.model)
# print(p2.battery_size)
# print(p2.get_brand())



# p3 = Car("tata","safari")
# p4 = Electric_car("mahindra","bex6","100kwh")

# p3.model = "xyxx"
# print(p3.model())


# print(p3.fuelType())
# print(p4.fuelType())
# print(Car.total_car)


# print(Car.car_description())
# print(Car.fuelType())


# multiple inheritance

class Battery():
    def batter_info(self):
        return " this is battery"
    
    

class Engine():
    def engine_life(self):
        return "car depends on engine life"


class ElecticCarTwo(Battery , Engine , Car):
    pass


my_new_tesla = ElecticCarTwo("mahindra","xuv7x0")
print(my_new_tesla.batter_info())
print(my_new_tesla.engine_life())





























# class Student:
#     def __init__(self):
#         self.__marks=0
    
#     def set_marks(self,value):
#         if value>=0 and value<=101:
#              self.__marks = value
#              return self.__marks
#         else:
#             return "invalid number"
            




# # s1 = Student(23)
# # print(s1.marks)

# s2 = Student()

# print(s2.set_marks(-67))