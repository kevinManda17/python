# coding:utf-8

# object oriented progamming :-----)> OOP

class Atome():

    'atomes simplifies, choisis parmi 10 premiers element du TP '

    table=[None,('hydrogene',0),('helium',2),('lithium',4),('beryllium',5),('bore',6),('carbone',6),('azote',7),('oxygene',8),('fluor',9),('neon0',10),('',10)]


    def __init__(self,nat):

        "le n` atomique determine le n` de protons d'electrons et neutrons "

        self.np , self.ne= nat , nat
        self.nn=Atome.table[nat][1]

    def afficher(self):

        print()
        print("Nom de l'element: ", Atome.table[self.np][0])
        print("{0} protons , {1} electrons,{2} neutrons ".format(self.np, self.ne,self.nn))

class Ion(Atome):

    'les ions sont les atomes qui ont gagne ou perdu des electrons'

    def __init__(self,nat, charge):

        "le n atomique et lea charge electrique determinent  l'ion "
        Atome.__init__(self,nat)
        self.ne=self.ne-charge
        self.charge= charge

    def afficher(self):

        Atome.afficher(self)
        print("particule electrisee. charge=",self.charge)


# programme principal

a1=Atome(5)
a2=Ion(3,1)
a3=Ion(8,-2)
a1.afficher()
a2.afficher()
a3.afficher()

print("---------------------------- la fin ----------------------------")
# help(Atome.table)
