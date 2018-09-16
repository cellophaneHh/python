import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
print(np.sin(x))
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# show()在一个会话中只能使用一次，通常放在脚本最后
plt.show()
