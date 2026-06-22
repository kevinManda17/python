from experta import KnowledgeEngine, Rule, Fact

class EnergyFact(Fact):
    pass

class EnergyExpertEngine(KnowledgeEngine):
    
    @Rule(EnergyFact(battery_level=P(lambda x: x < 20)))
    def low_battery(self):
        print("Attention: batterie faible ! Jarvis notifie l'utilisateur.")
    
    @Rule(EnergyFact(room_occupied=False))
    def turn_off_lights(self):
        print("Aucune présence détectée : extinction des lumières.")
    
    @Rule(EnergyFact(high_consumption=True))
    def alert_high_consumption(self):
        print("Consommation élevée détectée !")
