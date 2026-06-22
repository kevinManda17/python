from sympy import * 

x= Symbol('x')
expr = x 

res = integrate(1/x , (x, 1, E) )
print(res)

