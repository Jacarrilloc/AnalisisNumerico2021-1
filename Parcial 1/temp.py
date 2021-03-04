import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt

x  = sym.Symbol('x')
e =2.7182818284590
##fun = math.log(e,x+1)
fx = sym.cos(x)
muestras = 51
x0 = -5
grado = 2       
n  = grado + 1  
while (x0 < 5):
    k = float(0.005)
    polinomio = 0
    while (k < n):
        derivada   = fx.diff(x,k)
        derivadax0 = derivada.subs(x,x0)
        divisor   = np.math.factorial(k)
        terminok  = (derivadax0/divisor)*(x-x0)**k
        polinomio = polinomio + terminok
        k = k + 1
        plt.plot(k, x0)
    x0 = x0 + 1
print(polinomio)