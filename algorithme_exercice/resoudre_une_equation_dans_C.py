from sympy import * 

x= Symbol('x')
expr = x 

res = solve(x**2+x+1,x) 

print(res)