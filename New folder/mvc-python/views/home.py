"""
    HomeView
"""

import sys

# Accueil principal (menu)
def index():
    print("----------------------")
    print("Application Console")
    print("----------------------")
    print("1. Afficher animaux")
    print("2. Quitter")
    print("----------------------")

# Message de fin du programme
def exit():
    print("Fin du programme.")
    sys.exit(0)