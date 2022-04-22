import random
from random import randint 
station = ""
i = int(input("how many loops do you wish to test?"))
c = 0
visted = []
firstRoll = randint(1,11)
while c != i:
    random.seed()
    c += 1
    if(firstRoll == 1 or station == "GroundWater"):
        visted.append("ground water")
        dice = randint(1,6) 
        if dice in [1,3,5]:
            station = "SurfaceWater"
        elif dice in [2,4,6]:
            station = "Ocean"
        continue
    if(firstRoll == 2 or station == "Ocean"):
        visted.append("ocean")
        dice = randint(1,6)
        if dice in [1]:
            station = "GroundWater"
        elif dice in [2,3]:
            station = "LivePlant"
        elif dice in [4,5,6]:
            station = "Atmosphere"
        continue
    if(firstRoll == 3 or station == "Atmosphere"):
        visted.append("Atmosphere")
        dice = randint(1,6)
        if dice in [1,2,3,4]:
            station = "Soil"
        elif dice in [5,6]:
            station = "Rain"
        continue
    if(firstRoll == 4 or station == "AnimalWaste"):
        visted.append("Animal Waste")
        dice = randint(1,6)
        if dice in [1,2]:
            station = "Soil"
        elif dice in [3,4]:
            station = "Ferilizer"
        elif dice in [5,6]:
            station = "SurfaceWater"
        continue
    if(firstRoll == 5 or station == "LivePlant"):
        visted.append("living plants")
        dice = randint(1,6)
        if dice in [1,3,5]:
            station = "DeadOrganisms"
        elif dice in [2,4,6]:
            station = "LiveAnimal"
        continue
    if(firstRoll == 6 or station == "LiveAnimal"):
        visted.append("living animal")
        dice = randint(1,6)
        if dice in [1,3,5]:
            station = "DeadOrganisms"
        elif dice in [2,4,6]:
            station = "AnimalWaste"
        continue
    if(firstRoll == 7 or station == "DeadOrganisms"):
        visted.append("dead plants or animals")
        dice = randint(1,6)
        if dice in [1,2]:
            station = "Soil"
        elif dice in [3]:
            station = "SurfaceWater"
        elif dice in [4]:
            station = "Ocean"
        elif dice in [5,6]:
            station = "Atmosphere"
        continue
    if(firstRoll == 8 or station == "Ferilizer"):
        visted.append("fertilizer")
        dice = randint(1,6)
        if dice in [1,2]:
            station = "SurfaceWater"
        elif dice in [3,4]:
            station = "Soil"
        elif dice in [5,6]:
            station = "LivePlant"
        continue
    if(firstRoll == 9 or station == "Soil"):
        visted.append("soil")
        dice = randint(1,6)
        if dice in [1]:
            station = "GroundWater"
        elif dice in [2]:
            station = "SurfaceWater"
        elif dice in [3,4]:
            station = "LivePlant"
        elif dice in [5,6]:
            station = "Atmosphere"
        continue
    if(firstRoll == 10 or station == "Rain"):
        visted.append("rainwater")
        dice = randint(1,6)
        if dice in [1]:
            station = "SurfaceWater"
        elif dice in [2,3]:
            station = "Soil"
        elif dice in [4]:
            station = "GroundWater"
        elif dice in [5,6]:
            station = "Ocean"
        continue
    if(firstRoll == 11 or station == "SurfaceWater"):
        visted.append("surface water")
        dice = randint(1,6)
        if dice in [1,2]:
            station = "LivePlant"
        elif dice in [3,4]:
            station = "Ocean"
        elif dice in [5,6]:
            station = "GroundWater"
        continue
print(visted)