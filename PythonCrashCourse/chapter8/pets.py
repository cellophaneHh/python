def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置参数
describe_pet('hamster', 'harry')
describe_pet('dog', 'wangwang')

#关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet( pet_name='harry',animal_type='hamster')

def describe_pet(pet_name, animal_type='dog'):
    """默认值, 必须先列出没有默认值的形参"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='hehe')

#实参必须制定
#如下会报错
describe_pet()

