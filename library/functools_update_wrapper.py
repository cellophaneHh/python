'''
默认partial后的对象没有__name__和__doc__属性，
使用update_wrapper()可以将这些属性添加到partial对象

WRAPPER_ASSIGNMENTS元组中的属性被添加到partial对象中
WRAPPER_UPDATES中的值被更新到partial对象中
'''
import functools


def myfunc(a, b=2):
    'docstring for myfunc().'
    print(' called myfunc with: ', (a, b))


def show_details(name, f):
    'show details of a callable object.'
    print('{}:'.format(name))
    print(' object:', f)
    print(' __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print(' __doc__', repr(f.__doc__))
    try:
        print(' __module__', repr(f.__module__))
    except AttributeError:
        print('no __module__')
    try:
        print('__annotations__', repr(f.__annotations__))
    except AttributeError:
        print('no __annotations__')
    print()


show_details('myfunc', myfunc)


p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper:')

print(' assign:', functools.WRAPPER_ASSIGNMENTS)
print(' update:', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
