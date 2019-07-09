import numpy as np

np.random.seed(1024)
rating = np.random.randn(100).reshape(100, 1)
rating = np.around(rating, decimals=1) + [6]
time = np.random.randint(90, 144, size=100).reshape(100, 1).astype(int)
result = np.hstack((time, rating)).astype(str)
result = np.vstack((['time', 'rating'], result))
np.savetxt('./movie.csv', result, fmt='%s', delimiter=',')
print('finished')
