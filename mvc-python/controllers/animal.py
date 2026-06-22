"""
    AnimalController
"""

import models.animal as animal_model
import views.animal as animal_view

def show_all():
    all_animals = animal_model.AnimalService.get_all()
    animal_view.show(all_animals)