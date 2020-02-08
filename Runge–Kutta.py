import numpy as np
import matplotlib.pyplot as plt
"""
4次のルンゲ-クッタ法による1階常微分方程式
The fourth-order Runge-Kutta method for the 1st order ordinary differencial equation

dx/dt = -x^3+sin(t)を解く
"""

def f(x,t):
    return -x**3 +np.sin(t)

a = 0.0
b = 10.0
N = 100
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
x = 0.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f (x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)
    x += (k1+2*k2+2*k3+k4)/6

plt.plot (tpoints, xpoints)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()