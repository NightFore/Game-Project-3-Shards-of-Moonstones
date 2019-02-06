import random
from Tool import *

class Player:
    def __init__(self, name):
        self.name = name
        
        self.Level = 1
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.MaxMP      = 20
        self.MP         = self.MaxMP
        self.Strength   = 6
        self.Magic      = 2
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
PlayerIG = Player("NightFore")

class Wolf:
    def __init__(self, name):
        self.name = name

        self.Level = 1
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
WolfIG = Wolf("Wolf")




def Attack():
    Accuracy = (50 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed**2 / GameStateIG.Ennemy[0].Speed**2)
    Hit = random.randint(0, 100)
    print("Accuracy =", Accuracy)
    print("Hit =", Hit)
    if Accuracy >= Hit:
        GameStateIG.Ennemy[0].Health -= PlayerIG.Strength

def Magic():
    pass

def Guard():
    pass
