'''
装饰器函数，参数是和@my_decorator(params)参数中的params中一致的
然后返回的也是一个装饰器, 其参数是装饰器装饰的函数, 内部返回一个wrapper内对函数进行扩展
'''


def my_decorator(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("before... {}".format(name))
            print("func name: {}".format(func.__name__))
            result = func(*args, **kwargs)
            print("after...")
            return result

        return wrapper

    return decorator


@my_decorator(name="info")
def fuck_life():
    print('函数执行>>>>>>')


fuck_life()
