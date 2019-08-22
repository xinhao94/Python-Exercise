import math
import numpy as np
import matplotlib.pyplot as plt

def logStar(n):
  count = 0
  if n<=1:
    return count
  else:
    temp = n
    while temp>1:
      temp = math.log(temp,2)
      count += 1
    return count

x = np.linspace(0, 1000, 1000)
y = [logStar(i) for i in x]

plt.plot(x,y)
plt.show()
