from abc import ABC , abstractclassmethod

""" 
    boutons , etiquettes , champs de texte , tableaux
"""

class Widget(ABC):
    def test(self):
        print("Test !\n")

    @abstractclassmethod
    def render(self):
        pass

class Button(Widget):
    def render(self):
        print("Rendu d'un bouton")

class Label(Widget):
    def render(self):
        print("Rendu d'un etiquette...")

class TexteField(Widget):
    def test(self):
        print("Nouveau test !")

    def render(self):
        print("Rendu d'un champ de texte !")


btn= Button()
btn.test()
btn.render()

txf=TexteField()
txf.test()
txf.render()
