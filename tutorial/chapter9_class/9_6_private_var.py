"""
私有变量

在pytho中不存在只能从对象内部访问的”私有“实例变量，但是有一项大多数python代码都遵循的公约：带有下划线(例如__spam)前缀的名称被视为非公开的api的一部分

__spam形式的任何标识符(前面至少又两个下划线，后面至多一个下划线)，将被替换为_classname__spam,classsname是当前类名
"""

class Mapping:

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
         # 不能这么写，这样的话子类调用是会调用到子类的同名方法，但是定义不同，会有错误
        # self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # 私有变量，这个起到一个复制的作用，超类使用调用超类的方法

class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


my_map = MappingSubclass([x for x in range(1, 10)])

my_map.update([1], [2])

print(my_map.items_list)

