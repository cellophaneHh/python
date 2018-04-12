class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_descriptive_name(self):
        """打印里程"""
        print(str(self.odometer_reading))

    def increment_odd(self, odd):
        self.odometer_reading += odd


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_descriptive_name()

#继承
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def increment_odd(self):
        self.odometer_reading += 1

my_telsa = ElectricCar('tesla', 'model s', 2016)
print(my_telsa.get_descriptive_name())
my_telsa.increment_odd()
print(my_telsa.odometer_reading)
my_telsa.increment_odd(100)
#没有重载?
# print(my_telsa.odometer_reading)

