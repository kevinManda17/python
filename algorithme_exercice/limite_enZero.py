from sympy import * 

x= Symbol('x')
expr = x 

res = limit(1/(x+1), x, 0)
print(res)

