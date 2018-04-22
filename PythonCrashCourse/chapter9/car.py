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
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def increment_odd(self):
#         self.odometer_reading += 1

# my_telsa = ElectricCar('tesla', 'model s', 2016)
# print(my_telsa.get_descriptive_name())
# my_telsa.increment_odd()
# print(my_telsa.odometer_reading)
# my_telsa.increment_odd()
# #没有重载?
# # print(my_telsa.odometer_reading)



class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a ' + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """模拟电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()




