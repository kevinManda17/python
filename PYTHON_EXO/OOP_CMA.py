class  Point():
    
    "definition of geometric point "
  

p9=Point()

class Rectangle():

    "definition rectangle's class"

box=Rectangle()
box.length=50.0
box.width=35.0
box.wedge=Rectangle()
box.wedge.x=12.0
box.wedge.y=27.0

def findCenter(mybox):
    p=Point()
    p.x=mybox.wedge.x+mybox.width/2
    p.y=mybox.wedge.y+mybox.length/2
    
    return p

center=findCenter(box)

print(center.x, center.y)

box.length= box.length+20
box.width= box.width-5

center=findCenter(box)

print(center.x, center.y)

print(type(box.wedge.x))
print(type(box.wedge.y))
print(type(center))

print(type(p9))