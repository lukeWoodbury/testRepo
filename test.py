import matplotlib.pyplot as plt
import random

xs = [i for i in range(0,100)]

ys = [random.randint(0,100) for i in range(0,100)]

plt.scatter(xs,ys)
plt.savefig('fig.png')
plt.show()
