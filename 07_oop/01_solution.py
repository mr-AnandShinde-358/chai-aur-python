class Car:
    total_car=0
    def __init__(self,brand,Model):
        self.__brand=brand
        self.__model=Model
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric charage"
    
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())



# my_car = Car("Toyota","Corolla")




# print(Car())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)

# my_tesla = ElectricCar("Tesla","Model S","85KWH")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# print("fullname:",my_tesla.full_name(),"batteri size:",my_tesla.battery_size)

# print(my_tesla.__brand) # its private variable

# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())

# safari = Car("Tata","Safari")

# print(safari.fuel_type())

# My_car = Car("test","test")
# My_car.model="City"

# print(My_car.general_description())
# print(Car.general_description())
# print(Car.total_car)
# print(My_car.model)