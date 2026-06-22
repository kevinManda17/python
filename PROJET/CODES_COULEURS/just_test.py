
class Application():

    """creation de la classe des codes !"""

    def __init__(self,):

        """ Constructor main's Window"""

        self.root=Tk()
        self.root.title("KEVIN: Code Des Couleurs")
        self.dessineResistance()
        Label(self.root, text="Entrez la couleur de la resistance , en Ohms: ").\
        grid(row=2 , column=1, columnspan=3)
        Button(self.root, text="Montrer", command=self.changercouleurs,).\
        grid(row=3, column=0)
        Button(self.root, text="Quitter", command=self.root.quit).\
        grid(row=3, column=3)
        self.entree=Entry(self.root, width=14)
        self.entree.grid(row=3, column=2)
        # code couleus pour les valeurs de zero a neuf 
        self.cc=['black','brown', 'red','orange','yellow','green','blue','purple','grey','white']
        self.root.mainloop()

    def dessineResistance(self):

        """canevas avec un modelede resistance a trois lignes collorees"""

        self.can=Canvas(self.root, width=250,height=100, bg="ivory")
        self.can.grid(row=1,column=1, columnspan=3, padx=5,pady=5)
        self.can.create_line(10,50,240,50, width=5)
        self.can.create_rectangle(65,30,185,70, fill="light grey", width=2)
        # dessin des trois lignes colorees noires au depart 
        self.ligne=[]         #on memorise les  trois couleurs dans la liste 1
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70, fill='black', width=0))
    
    def changercouleurs(self):

        """ affichage des couleurs correspondant a la valeur entree"""

        self.v1ch=self.entree.get()
        try:
            v=float(self.v1ch)
        except:
            err=1
        else:
            if err ==1 or v< 10 or v > 1e11:
                self.signalErreur()
            else :
                li=[0]*3
                logv=int(log10(v))
                ordgr=10**logv
                # les premiers chiffres significatif
                li[1]=int(v/logv)
                decim=v/ordgr- li[0]
                # le second chiffre significatif 
                li[1]=int(decim*10+0.5)
                li[2]=logv-1
                for n in range(3):
                    self.can.itemconfigure(self.ligne[n], fill=self.cc[li[n]])

    def signalErreur(self):

        self.entree.configure(bg="red")
        self.root.after(1000, self.videEntree)

    def videEntree(self):

        self.entree.configure(bg='white')
        self.entree.delete(0, len(self.v1ch))

if __name__ == "__main__":

    # import wxPython
    from tkinter import *
    from math import log10
    f=Application()