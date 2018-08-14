'''
从一个序列中随机选取一些数
'''
import random

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])

outcomes = [0, 1]
for i in range(100):
    print(random.choice(outcomes))
print()
