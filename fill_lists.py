from math import sqrt, pi, exp

def h(x):
  return (1/(sqrt(2*pi))) * exp(-0.5*x**2)

i = 8/40
xlist = [-4 + i * n for n in range(41)]
hlist = [h(x) for x in xlist]
pairs = list(zip(xlist, hlist))

print(pairs)