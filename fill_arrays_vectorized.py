from numpy import sqrt, pi, exp, linspace


def h(x):
  return (1/(sqrt(2*pi))) * exp(-0.5*x**2)

xlist = linspace(-4,4,41)
hlist = h(xlist)
pairs = list(zip(xlist,hlist))

print(pairs)