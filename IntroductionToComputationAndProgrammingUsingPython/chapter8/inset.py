class IntSet():
    """整数集合"""
    # 关于实现(不是抽象)的信息
    # 集合的值由一个整数数组self.vals表示
    # 集合n中的每个整数在self.vals中只出现一次

    def __init__(self):
        """创建一个空数组"""
        self.vals = []

    def insert(self, e):
        """假设e是整数，将e插入self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """假设e是整数如果e在self中，则返回True，否则False"""
        return e in self.vals

    def remove(self, e):
        """假设e是整数，如果e在self中，则删除，否则抛出ValueError异常"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """返回一个包含self中元素的列表对元素不排序"""
        return self.vals[:]

    def __str__(self):
        """string"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'  # -1是为了截取最后的逗号

print(type(IntSet), type(IntSet.insert))

s = IntSet()
s.insert(3)
s.insert(4)
print(s)
