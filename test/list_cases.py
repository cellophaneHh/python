def logwrapper(level='info') -> (str):
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


l = [1, 2, 3]
func(*l)
