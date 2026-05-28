import matplotlib.pyplot as plt 
import numpy as np 

def f(x):
  return x*x

def g(x):
  return np.cos(x)

def h(x):
  return (x-3)

x = np.linspace(0, 2*np.pi, 100)
plt.figure(1)

plt.subplot(221)
plt.plot(x, f(x))
plt.title('f(x) = x * x')

plt.subplot(222)
plt.plot(x, g(x))
plt.title('g(x) = cos(x)')

plt.figure(2)

plt.plot(x, h(x))
plt.title('h(x) = x - 3')

plt.show
