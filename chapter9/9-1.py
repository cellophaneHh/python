class Restaurant():
    """餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("name:" + self.restaurant_name)
        print('type:' + self.cuisine_type)

    def open_restaurant(self):
        print("正在营业")

    def set_number_served(self, num):
        self.number_served = num

my_restaurant = Restaurant('一间旅馆', '大酒店')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(my_restaurant.number_served)
my_restaurant.number_served = 100
print(my_restaurant.number_served)
my_restaurant.set_number_served(1000)
print(my_restaurant.number_served)
