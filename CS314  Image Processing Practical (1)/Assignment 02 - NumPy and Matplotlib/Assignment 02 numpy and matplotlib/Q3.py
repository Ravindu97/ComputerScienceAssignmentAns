import matplotlib.pyplot as plt
import numpy as np
import math

### part a)

x = np.arange(0,math.pi,0.1)

#print(x)

### part b)

y = []

for i in x:
    y.append(5*math.sin(i) - 12)

#print(y)


plt.plot(x,y)
#plt.show()


### part c)

t = np.arange(0,6,0.1)

f= 2*t + 3

#print(f)


### part d)

plt.subplot(1,2,1)
plt.plot(x,y,'ro')
plt.xlabel("x - Axis")
plt.ylabel("y - Axis")

plt.subplot(1,2,2)
plt.plot(t,f,'gs')
plt.xlabel("t - Axis")
plt.ylabel("f - Axis")

plt.show()






