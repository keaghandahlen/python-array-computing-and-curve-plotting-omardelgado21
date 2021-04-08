from numpy import sqrt, pi, exp, linspace
import matplotlib.pyplot as plt

def h(x):
  return (1/(sqrt(2*pi))) * exp(-0.5*x**2)

xlist = linspace(-4,4,41)
hlist = h(xlist)

plt.plot(xlist,hlist,'-',markerfacecolor='none')
plt.xlim(-4,4)
plt.title('Gaussian Plot')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.show() 