"""
求近似平方根
"""

# 穷举法
x = 25
epsilon = 0.01
step = epsilon ** 2
numGuess = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuess += 1

print("numGuess = ", numGuess)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)


# 二分查找
x = 25
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuess)
print(ans, 'is close to square root of', x)

# 牛顿-拉夫森法寻找平方根
# 寻找x， 满足x**2 - 24 在epsilon和0之间
epsilon = 0.01
k = 25.0
guess = k/2.0
numGuess = 0
while abs(guess*guess - k) >= epsilon:
    numGuess += 1
    guess = guess - (((guess**2) - k)/(2*guess))

print('numGuess =', numGuess)
print(guess)

