from random import randint 
station = ""
i = int(input("how many loops do you wish to test?"))
c = 1
visted = []
while c != i:
    firstRoll = randint(1,10)
    if(firstRoll == 1 or station == "GroundWater"):
        visted.append("ground water")