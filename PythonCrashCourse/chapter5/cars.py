cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#不想区分大小写时，使用upper或者lower函数

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())

print(car, car.upper(), car)
