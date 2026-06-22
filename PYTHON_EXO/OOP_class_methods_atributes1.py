# learn OOP :object oriented  programming 

class  Point():

    "definition of geometric point "
  

p9=Point() # create an objet for class Point
p9.x=3.0
p9.y=4.0

def display_point(p):
    print("Coord. horintale=",p.x,"Coord. verticale=",p.y)
display_point(p9)

p1=Point()
p1.x=3
p1.y=4
p2=Point()
p2.x=3
p2.y=4
print("Not the same class's object: ",p1==p2)

# way to confirm  with our memory emplacement 
print("here is  p1's emplacement memory :",p1)
print("here is  p2's emplacement memory :",p2)

p1=p2
print("we give p1's value to p2: ",p1==p2)
p1.x=20 
print("other way to prove:",p2.x)
way1="here is  p1's emplacement memory == p2's emplacement memory:"
way2="here is  p2's emplacement memory == p1's emplacement memory :"
print(way1,p1)
print(way2,p2)

print("--------------------------------------------------- Other Part------------------------------------------------------------------------")
# help()