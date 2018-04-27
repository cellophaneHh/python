def fib(n):
    """
    n是非负数，返回第n个斐波那契数
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fast_fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try :
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result
        return result

print(fast_fib(120))
