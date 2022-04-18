from random import randint 
station = ""
i = int(input("how many loops do you wish to test?"))
c = 1
while c != i:
    firstRoll = randint(1,10)
    if(firstRoll == 1 or station == "GroundWater"):
        