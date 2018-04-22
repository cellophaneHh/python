#传递任意个数的实参: *params

def make_pizza(*toppings):
    """打印顾客点的所有配件"""
    print(type(toppings))
    print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(*toppings):
#     """概述要制作的披萨"""
#     for topping in toppings:
#         print("- " + topping)

# make_pizza('mushrooms', 'green peppers', 'extra cheese')
