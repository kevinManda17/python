from sympy import *

x= Symbol('x')
expr = x ** 2 
res = series(expr , x , 0 , 8 )
print(res)