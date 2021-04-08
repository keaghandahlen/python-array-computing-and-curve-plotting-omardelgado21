import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()

x = np.linspace(-6,6,200)
t = np.linspace(-1,1,200)
f = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*((x-3*t)))

fig = plt.figure()
lines = plt.plot(x,t)
plt.axis([x[0], x[-1], -1,1])
plt.xlabel('x')
plt.ylabel('f')

# #def init():
#   lines[0].set_data([],[])
#   return lines

def frame(args):
  t = args
  y = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*((x-3*t)))
  lines[0].set_ydata(y)
  return lines


anim = FuncAnimation(fig, frame, frames = t, interval = 30)
anim.save("wave.gif","imagemagick")

# def f(x,t):
#   return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*((x-3*t)))

# x = np.linspace(-6,6,1000)
# t_values = np.linspace(-1,1,60)

# counter = 0
# for t in t_values:
#   y = f(x,t)
#   plt.plot(x, y, "-", label=f"t={t:.2f}")
#   plt.xlabel(x)
#   plt.ylabel(f)
#   plt.legend()
#   counter += 1
#   #time.sleep(0.2)
# plt.show()

# lines = plot(x, y1, x, y2, x, y3)
# for parameter in parameters:
#   y1 = ...
#   y2 = ...
#   y3 = ...
#   for line, y in zip(lines, [y1, y2, y3]):
#     line.set_ydata(y)
#   plt.draw()