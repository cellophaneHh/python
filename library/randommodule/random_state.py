import random
import os
import pickle

if os.path.exists('state.dat'):
    # restore the previously saved state
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    # 记录
    random.setstate(state)
else:
    print('No state.dat, seeding')
    random.seed(1)

for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()


# 存储
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

print('\nAfter saving state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
