from math import *
from turtle import *
n=int(input('entrez une valeur: '))
a=int(input("entrez une valeur: "))
m=int(int(input("entrez une valeur: ")))
for i in range(n):
    x0=-3*i*a/2
    for j in range(m):
        y0=a*sqrt(3)*(1/2.*(i%2)-j)
        up()
        goto(-x0,-y0)
        down()
        for k in range(6):
            forward(a)
            left(60)