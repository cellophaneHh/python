from random import randint

x = randint(1, 5)
print(x)

class Die():
    """色子"""
    def __init__(self, sides = 6):
        self.sides = sides

    def rol_die(self):
        """返回一个1-色子面数的整数"""
        print(randint(1, self.sides))

my_die = Die(6)

for i in range(0, 10):
    my_die.rol_die()
