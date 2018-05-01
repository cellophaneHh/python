'''
nonlocal 在当前作用域中重新绑定一个上级作用域中的变量
global 将当前变量变为全局作用域的
'''
def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = 'test spam'
    do_local()  # 直接在函数中给变量复制，只在函数中起效，原来的变量不变
    print("After local assignment:", spam)
    do_nonlocal()  # 利用nonlocal，在函数的局部作用域中重新绑定一个变量
    print("After nonlocal assignment:", spam)
    do_global()  # 利用global，将变量变为全局的
    print("After global assignment:", spam)


scope_test()
print('In global scope:', spam)

