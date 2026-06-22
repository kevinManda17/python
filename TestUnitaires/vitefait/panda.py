#coding:utf-8

"""
Classe qui represente un panda 
   >>> isinstance(Panda("kiko", 21), Panda)
True 

"""

class Panda():
    def __init__(self, name , age):
        
        self.name= name 
        self.age= age 
        self.hunger = 50 
    
    """
    >>> panda.get_number()
    50
    """
    def get_number():
        return 50
    def __str__(self):
        return f"[Nom:{self.name} / age:{self.age} / Faim:{self.hunger}/100]"
    
    def eat(self,food_points):
        if self.hunger >= 100:
            print(f"{self.name} a deja bien mange (faim : {self.hunger})")
        else:
            self.hunger += food_points
            if self.hunger > 100:
                print("Quel festin !")
                self.hunger = 100 

            print(f"{self.name} vient de manger (faim: {self.hunger })")

    def task(self):
        print("Nioww !")

    def sleep(self):
        print("ZzzzZzzZzz")

if __name__ == "__main__":
    import doctest 
    doctest.testmod()
    # doctest.testfile("<fichier.txt>")
