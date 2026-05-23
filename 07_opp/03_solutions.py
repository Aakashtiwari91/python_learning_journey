class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
    @staticmethod
    def add(a,b):
        return a+b
p1 = Car("toyota","camry")

print(Car.add(3,4))