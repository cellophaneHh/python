"""
浮点型
decimal
"""
from decimal import *

# 计算70分钟电话费的5%税计算

print(round(Decimal('0.70') * Decimal('1.05'), 2))

print(round(0.70 * 1.05, 2))

# 设置精度
getcontext().prec = 36
d = Decimal(1) / Decimal(7)
print(d)

