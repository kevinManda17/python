"""
    HomeController
"""

import views.home as home_view

def index():
    while True:
        home_view.index()
        choice = int(input("> ")) # Saisie à vérifier !

        if choice == 1:
            import controllers.animal as animal_controller
            animal_controller.show_all()
        elif choice == 2:
            exit()
        else:
            print("Commande introuvable")

def exit():
    return home_view.exit()