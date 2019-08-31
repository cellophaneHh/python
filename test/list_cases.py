from typing import Callable


def logwrapper(level='info') -> Callable:
    print('level: {}'.format(level))

    def log(func):
        def wrapper(*args, **kwargs):
            print('前')
            result = func(*args, **kwargs)
            print('后')
            return result

        return wrapper

    return log


@logwrapper(level='debug')
def func(*params):
    print(params)


my_list = [1, 2, 3]
func(*my_list)
