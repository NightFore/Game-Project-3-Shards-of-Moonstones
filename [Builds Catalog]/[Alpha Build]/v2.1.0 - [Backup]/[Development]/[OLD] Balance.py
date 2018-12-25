import random
from Tool import *

class Player:
    def __init__(self, name):
        self.name = name
        
        self.Level = 1
        self.Experience = 0
        
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
    # Hit Chance
    Accuracy = (50 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed**2 / GameStateIG.Ennemy[0].Speed**2)
    Hit = random.randint(0, 100)

    if Accuracy >= Hit:
        # Damage
        GameStateIG.Ennemy[0].Health -= PlayerIG.Strength
        Sound("Attack")

        # HP Loss Cap
        if GameStateIG.Ennemy[0].Health < 0:
            GameStateIG.Ennemy[0].Health = 0
            

def Magic():
    pass

def Potion():
    pass


def Sound(Action):
    # Attack
    if Action == "Attack":
        Sound = random.randrange(1,2)
        
        # Defeated
        if GameStateIG.Ennemy[0].Health <= 0:
#or GameStateIG.Ennemy[1].Health <= 0 or GameStateIG.Ennemy[2].Health <= 0
            Sound_Defeated.play()

        # Damage
        elif Sound == 1:
            Sound_Hit_Damage_1.play()
        elif Sound == 2:
            Sound_Hit_Damage_2.play()
        Action = ""
