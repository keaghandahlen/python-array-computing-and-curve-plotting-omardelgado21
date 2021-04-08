import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-4,4,1000)
t=0
f=np.exp(-(X-3*t)**2)*np.sin(3*np.pi*((X-3*t)))

plt.plot(X,f)
plt.xlabel('X')
plt.ylabel('f(x,t)')
plt.show()