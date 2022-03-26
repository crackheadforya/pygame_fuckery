import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 18+np.sin(x) + np.random.normal(scale=0.2, size=len(x))


x = np.linspace(1,64)
plt.ylim(0,36)

plt.plot(x, f(x))

plt.show()