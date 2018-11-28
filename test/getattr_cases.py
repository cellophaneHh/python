'''
根据函数名,获得方法
'''


class User:

    @staticmethod
    def show():
        print('123')


method = getattr(User, 'show')
print(type(method))
method()
