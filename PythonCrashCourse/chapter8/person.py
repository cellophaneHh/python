#if的条件会根据bool(param)函数返回值判断不是布尔的数据的布尔值
def build_person(first_name, last_name, age=''):
    """返回字典"""
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', '10')
print(musician)

del musician['age']
print(musician)
