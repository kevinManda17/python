# learn OOP : object oriented  programming 

class Point():
    
    "definition of a geometric point "


p9=Point() # create an objet for class Point
p9.x=3.0
p9.y=4.0

Carre= p9.x**2+p9.y**2



print("x:",p9.x,"\n");  print("y:",p9.y,"\n"); print(" sum(x*x + y*y) or x** and y** :",Carre,"\n")

# print([p9])  #return  an instance of class Point() and is in memory emplacement 
# print(p9.__doc__) # return definition of class
# help(Point)
print("--------------------------------------- training -----------------------------------------------------")

# importation string's modul 
import string 

str_cap=string.capwords 
print(str_cap) 
    
str_upper=string.ascii_uppercase
for lettre in str_upper:
    print(lettre, end="\t\t")
print()

str_punc=string.punctuation
print(str_punc)

str_hexD=string.hexdigits
print(str_hexD)

help(string)