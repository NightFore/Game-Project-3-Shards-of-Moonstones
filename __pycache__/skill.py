from Balance import *

def heal():
   if (PlayerIG.MP - 10 + (2 * (PlayerIG.Level - 1))) >= 0
        PlayerIG.Health += 8 + (2 * (PlayerIG.Level - 1))
        PlayerIG.MP -= 10 + (2 * (PlayerIG.Level - 1))
        if PlayerIG.Health >= PlayerIG.Maxhealth:
            PlayerIG.Health = PlayerIG.Maxhealth
   else:
        pass

def Boost():
    if (PlayerIG.MP - 7 - (2 * (PlayerIG.Level - 1))) >= 0 :                 
        PlayerIG.Strength += 2 + (1 * (PlayerIG.Level - 1)) 
        PlayerIG.Speed += 2 + (1 * (PlayerIG.Level - 1))
        PlayerIG.MP -= 7 - (2 * (PlayerIG.Level - 1))
    else:
        pass
def Charging():
    if (PlayerIG.Health - PlayerIG.Maxhealth * (1/4)) >= 0:
        HitC = random.randint(0, 100)
        CritC = (10 + (0.5*PlayerIG.Level)) * (PlayerIG.Speed*PlayerIG.Strength) / (GameStateIG.Ennemy[0].Defense*PlayerIG.Defense*5)
        if CritC > HitC:
            GameStateIG.Ennemy[0].Health -= PlayerIG.Strength*4
        else:
            GameStateIG.Ennemy[0].Health -= PlayerIG.Strength*3
        PlayerIG.Health -= PlayerIG.Maxhealth * (1/4)
    else:
        pass

def Fireball():
    if PlayerIG.MP - 10 - (2 * (PlayerIG.Level - 1)) >= 0:
        GameStateIG.Ennemy[0].Health -= PlayerIG.Magic
        PlayerIG.Magic += 1
        PlayerIG.MP -= 10 - (2 * (PlayerIG.Level - 1))
    else:
        pass
