import datetime

class Person():

    def __init__(self, name):
        """人"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """全名"""
        return self.name

    def getLastName(self):
        """姓"""
        return self.lastName

    def setBirthday(self, birthday):
        """生日"""
        self.birthday = birthday

    def getAge(self):
        """年龄"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """如果self按字母顺序排在other前面，则返回True，否则返回False, 重载了<运算符"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """返回全名"""
        return self.name

me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')

print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')


pList = [me, him, her]
for p in pList:
    print(p)

pList.sort()
for p in pList:
    print(p)
