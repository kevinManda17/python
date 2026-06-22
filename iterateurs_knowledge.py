li = [1,2,3,4,5]

iterator = iter(li)


while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class R_iter():
    def __init__(self, end):
        if end <=0 :
            raise ValueError("Point d'arret de l'intervale invalide !")
        self.current = 0
        self.end = end 

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current +=1 

        if self.current > self.end :
            raise StopIteration
        
        return self.current -1
    
ran  = R_iter(5)

for v in ran :
    print(v)


class Inventory :
    def __init__(self, name):
        self.name = name 
        self.content= []

    def __iter__(self):
        return iter(self.content)
    
    def __next__(self):
        return next(self.content)

    def  add(self, item ):
        self.content.append(item)

chest = Inventory("Large malle")

chest.add("Epee en bois ")
chest.add("Potion de soins mineurs")
chest.add("Marque d'honneur")

for item in chest:
    print(item)
