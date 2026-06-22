from sympy import * 

x , y = symbols('x y')
res = solve([2*x+y-2,-3*x-5*y-1],[x,y]) 
print(res)