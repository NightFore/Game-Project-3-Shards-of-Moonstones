import random
from Tool import *



class NoMonster:
    def __init__(self, name):
        self.name = name
        self.Icon   = NoMonster_Icon
        self.Img    = NoMonster_Img

        self.Level      = 1
        self.EXP_Gain   = 0
        self.Gold_Gain  = 0
        self.Action_Point = 0
        
        self.Maxhealth  = 0
        self.Health     = self.Maxhealth
        self.Strength   = 0
        self.Magic      = 0
        self.Speed      = 0
        self.Defense    = 0
        self.Resistance = 0
NoMonsterIG = NoMonster("NoMonster")
GameStateIG.Enemy  = [NoMonsterIG,NoMonsterIG,NoMonsterIG]



class Player:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Ellesia_Icon
        self.Img    = Ellesia_Img
        self.Class  = "Lancer"
        
        self.Level      = 1
        self.Experience = 0
        self.Gold       = 0
        self.Action_Point = 100
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
PlayerIG = Player("NightFore")



class Iris:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Iris_Icon
        self.Img    = Iris_Img
        self.Class  = "Archer"
        
        self.Level      = 1
        self.Experience = 0
        self.Action_Point = 0
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
IrisIG = Iris("Iris")



class Gyrei:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Gyrei_Icon
        self.Img    = Gyrei_Img
        self.Class = "Dual Wielder"
        
        self.Level      = 1
        self.Experience = 0
        self.Action_Point = 0
        
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.Strength   = 6
        self.Magic      = 10
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
GyreiIG = Gyrei("Gyrei")





class Wolf:
    def __init__(self, name):
        self.name   = name
        self.Icon   = Wolf_Icon
        self.Img    = Wolf_Img

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 10 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0

        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
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

        self.Level      = 1
        self.EXP_Gain   = 10
        self.Gold_Gain  = 10
        self.Action_Point = 0
        
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
Shadow_Figure2IG = Shadow_Figure2("Shadow_Figure2")



def Attack(Selection):
    GameStateIG.Attack_Choice = False
    
    # Hit Chance
    Accuracy = (50 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed**2 / GameStateIG.Enemy[Selection].Speed**2)
    Hit = random.randint(0, 100)
    Crit = (10 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed*PlayerIG.Strength) / (GameStateIG.Enemy[Selection].Defense*PlayerIG.Defense*5)
    if Accuracy >= Hit:
        if Crit>=Hit:
        # Damage
            GameStateIG.Enemy[Selection].Health -= PlayerIG.Strength*2
        else:
            GameStateIG.Enemy[Selection].Health -= PlayerIG.Strength
        Sound("Attack")

        # HP Loss Cap
        if GameStateIG.Enemy[Selection].Health < 0:
            GameStateIG.Enemy[Selection].Health = 0
    print(GameStateIG.Enemy[Selection].Health)
            
def Skill():
    pass
                             
def Potion():
    pass


def Sound(Action):
    # Attack
    if Action == "Attack":
        Sound = random.randrange(1,2)
        
        # Defeated
        if GameStateIG.Enemy[0].Health <= 0 and GameStateIG.Enemy_Death[0] == False or GameStateIG.Enemy[1].Health <= 0 and GameStateIG.Enemy_Death[1] == False or GameStateIG.Enemy[2].Health <= 0 and GameStateIG.Enemy_Death[2] == False:
            Sound_Defeated.play()

        # Damage
        elif Sound == 1:
            Sound_Hit_Damage_1.play()
        elif Sound == 2:
            Sound_Hit_Damage_2.play()
        Action = ""



############################
##    self.Turn_Check = [0,0,0,0,0,0]
##    self.Turn_Order =  [GameStateIG.Character[0],GameStateIG.Character[1],GameStateIG.Character[2],
##                        GameStateIG.Character[3],GameStateIG.Character[4],GameStateIG.Character[5]]
##                        #[GameStateIG.Player[1].AP,GameStateIG.Player[2].AP,GameStateIG.Player[3].AP,
##                        #GameStateIG.Enemy[1].AP,GameStateIG.Enemy[2].AP,GameStateIG.Enemy[3].AP]
##
##
##    self.Character #Player/Enemy
##    self.Type = "Player"
##    self.Type = "Monster"

##    self.Select_Attack = ""



def Action_Point():
    Maxi = Maximum(GameStateIG.Turn_Order, "Index")
    
    if GameStateIG.Turn_Order[Maxi] < 100:
        for x in range(6):
            GameStateIG.Turn_Order[x] += GameStateIG.Character[x].Speed

    elif GameStateIG.Turn_Order[Maxi] >= 100:
        GameStateIG.Turn_Order[Maxi] -= 100
        GameStateIG.Turn_Check[Maxi] += 1
        GameStateIG.Turn_Phase = GameStateIG.Character[Maxi]

        if all(i>0 for i in GameStateIG.Turn_Check):
            GameStateIG.Turn_Count += 1
            Turn_Check = [0,0,0,0,0,0]
            
        Action(Maxi)

def Action(Maxi):
    if "Player" in GameStateIG.Character[Maxi]:
        pass
    elif "Monster" in GameStateIG.Character[Maxi]:
        pass

def Action_Choice():
    if None:
        GameStateIG.State_Fight = "Attack"
        Attack()
        
    if None:
        GameStateIG.State_Fight = "Skill"
        Skill()
        
    if None:
        GameStateIG.State_Fight = "Defend"
        Defend()





def Maximum(Liste, Type):
    Maxi = 0
    Index  = -1
    for i in Liste:
        if i > Maxi:
            Maxi = i
            Index += 1
            
    if Type == "Index":
        return Index
    else:
        return Maxi

def Minimum(Liste, Type):
    Mini = 0
    Index  = -1
    for i in Liste:
        if i < Mini:
            Mini = i
            Index += 1
            
    if Type == "Index":
        return Index
    else:
        return Mini

