class InfoHiding:

    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__inVisible = 'Don\'t look at me directly'

    def printVisible(self):
        print(self.visible)

    def printInvisible(self):
        print(self.__inVisible)

    def __printInvisible(self):
        print(self.__inVisible)

    def __printInvisible__(self):
        print(self.__inVisible)

test = InfoHiding()

print(test.visible)
print(test.__alsoVisible__)

print(test.__inVisible)  # 访问不到
