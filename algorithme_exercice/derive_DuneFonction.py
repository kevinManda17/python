from sympy import *

x = Symbol('x')
expr= x**2 +2*x
res= diff(expr, x )
print(res)