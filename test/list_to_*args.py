'''
测试列表转换为可变长参数
'''

def foo(*args):
    print(args)
    print(type(args))
    for a in args:
        print(a)


names = ['1', '2', '3']
foo(*names)
