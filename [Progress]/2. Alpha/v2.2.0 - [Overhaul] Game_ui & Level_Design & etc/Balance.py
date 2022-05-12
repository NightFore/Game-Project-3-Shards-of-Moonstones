import random
from Tool import *


class Player:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Ellesia_Icon
        self.Img    = Ellesia_Img
        
        self.Level = 1
        self.Experience = 0
        self.Gold = 0
        self.Class = "Lancer"
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.MaxMP      = 20
        self.MP         = self.MaxMP
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
PlayerIG = Player("NightFore")
GameStateIG.Player[0] = PlayerIG



class Iris:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Iris_Icon
        self.Img    = Iris_Img
        
        self.Level = 1
        self.Experience = 0
        self.Class = "Archer"
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.MaxMP      = 20
        self.MP         = self.MaxMP
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
IrisIG = Iris("Iris")
GameStateIG.Player[1] = IrisIG



class Gyrei:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Gyrei_Icon
        self.Img    = Gyrei_Img
        
        self.Level = 1
        self.Experience = 0
        self.Class = "Dual Wielder"
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.MaxMP      = 20
        self.MP         = self.MaxMP
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
GyreiIG = Gyrei("Gyrei")
GameStateIG.Player[2] = GyreiIG






class NoMonster:
    def __init__(self, name):
        self.name = name
        self.Icon   = NoMonster_Icon
        self.Img    = NoMonster_Img

        self.Level = 1
        self.Experience_Gain = 0
        self.Gold_Gain = 0

        self.Health = 0
        
NoMonsterIG = NoMonster("NoMonster")
GameStateIG.Enemy  = [NoMonsterIG,NoMonsterIG,NoMonsterIG]


class Wolf:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Wolf_Icon
        self.Img    = Wolf_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 120 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
WolfIG = Wolf("Wolf")


class Direwolf:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Direwolf_Icon
        self.Img    = Direwolf_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
DirewolfIG = Direwolf("Direwolf")


class Spectre:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Spectre_Icon
        self.Img    = Spectre_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
SpectreIG = Spectre("Spectre")


class Shadow_Figure1:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Shadow_Figure1_Icon
        self.Img    = Shadow_Figure1_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
Shadow_Figure1IG = Shadow_Figure1("Shadow_Figure1")


class Summoner:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Summoner_Icon
        self.Img    = Summoner_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
SummonerIG = Summoner("Summoner")


class Zombie:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Zombie_Icon
        self.Img    = Zombie_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        

        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
ZombieIG = Zombie("Zombie")


class Ghoul:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Ghoul_Icon
        self.Img    = Ghoul_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
GhoulIG = Ghoul("Ghoul")


class Shadow_Figure2:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Shadow_Figure2_Icon
        self.Img    = Shadow_Figure2_Img

        self.Level = 1
        self.Experience_Gain = 10
        self.Gold_Gain = 10
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
Shadow_Figure2IG = Shadow_Figure2("Shadow_Figure2")





def Attack():
    # Hit Chance
    Accuracy = (50 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed**2 / GameStateIG.Enemy[0].Speed**2)
    Hit = random.randint(0, 100)
    Crit = (10 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed*PlayerIG.Strength) / (GameStateIG.Enemy[0].Defense*PlayerIG.Defense*5)
    if Accuracy >= Hit:
        if Crit>=Hit:
        # Damage
            GameStateIG.Enemy[0].Health -= PlayerIG.Strength*2
        else:
            GameStateIG.Enemy[0].Health -= PlayerIG.Strength
        Sound("Attack")

        # HP Loss Cap
        if GameStateIG.Enemy[0].Health < 0:
            GameStateIG.Enemy[0].Health = 0
            
def Skill():
    pass
                             
def Potion():
    pass


def Sound(Action):
    # Attack
    if Action == "Attack":
        Sound = random.randrange(1,2)
        
        # Defeated
        if GameStateIG.Enemy[0].Health <= 0:
#or GameStateIG.Enemy[1].Health <= 0 or GameStateIG.Enemy[2].Health <= 0
            Sound_Defeated.play()

        # Damage
        elif Sound == 1:
            Sound_Hit_Damage_1.play()
        elif Sound == 2:
            Sound_Hit_Damage_2.play()
        Action = ""
