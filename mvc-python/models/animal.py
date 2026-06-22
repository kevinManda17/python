"""
    AnimalModel
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} est un animal âgé de {self.age} an(s)."


class AnimalService:
    @staticmethod
    def get_all():
        animals = []

        with open("_data/animals.txt", "r", encoding = "utf8") as f:
            lines = f.read().splitlines()
            for line in lines:
                attributes = line.split(" ")
                a = Animal(attributes[0], attributes[1])
                animals.append(a)

        return animals