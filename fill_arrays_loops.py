from numpy import sqrt, pi, exp, zeros 


def h(x):
  return (1/(sqrt(2*pi))) * exp(-0.5*x**2)

n = 8/40
xlist = zeros(41,float)
hlist = zeros(41,float)

for i in range(41):
    xlist[i] = -4 + i*n
    hlist[i] = h(xlist[i])
    
pairs = list(zip(xlist,hlist))
print(pairs)