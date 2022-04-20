from random import randint 
station = ""
i = int(input("how many loops do you wish to test?"))
c = 1
visted = []
while c != i:
    firstRoll = randint(1,10)
    if(firstRoll == 1 or station == "GroundWater"):
        visted.append("ground water")
        dice = randint(1,6) 
        if dice in [1,3,5]:
            station = "Surface Water"
        elif dice in [2,4,6]:
            station = "ocean"
        continue
    if(firstRoll == 2 or station == "Ocean"):
        visted.append("ocean")
        dice = randint(1,6)
        if dice in [1]:
            station = "GroundWater"
        elif dice in [2,3]:
            station = "LivePlant"
        elif 