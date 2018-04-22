#有返回值，通过设置默认值让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """获得整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'dd')
print(musician)
