class Test():
    def __init__(self,name):
        self.ABC = [1,2,3,4,5,6]
TestIG = Test("Test")

class GameState():
    def __init__(self,name):
        self.Turn_Order = [20,30,40,1650,60,151]
        self.Player = [20,20,20]
        self.Enemy = [20,20,20]
        self.PlayerTest = ["Player","Player","Player","Monster","Player","Player"]
GameStateIG = GameState("GameState")

class Player():
    def __init__(self,name):
        self.Character = [GameStateIG.PlayerTest[0],
                          GameStateIG.PlayerTest[1],
                          GameStateIG.PlayerTest[2],
                          GameStateIG.PlayerTest[3],
                          GameStateIG.PlayerTest[4],
                          GameStateIG.PlayerTest[5]]
PlayerIG = Player("Player")


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


def Action_Point():
    Maxi = Maximum(GameStateIG.Turn_Order, "Index")
    if GameStateIG.Turn_Order[Maxi] < 100:
        for x in range(3):
            GameStateIG.Turn_Order[x]   += GameStateIG.Player[x]
            GameStateIG.Turn_Order[x+3] += GameStateIG.Enemy[x]

    elif GameStateIG.Turn_Order[Maxi] >= 100:
        GameStateIG.Turn_Order[Maxi] -= 100

        Action(Maxi)


def Action(Maxi):
    if "Player" in PlayerIG.Character[Maxi]:
        print(GameStateIG.Character[Maxi])
        print("Player")
    else:
        print("Monster")
Action_Point()









Test = [1,2,3,4,5,6]
Test_1 = all(i>0 for i in Test)
Test_2 = all(i>1 for i in Test)

if Test_1 == True:
    print("Test 1 : Success")
else:
    print("Failure")

if Test_2 == True:
    print("Success")
else:
    print("Test 2 : Failure")
