P1G = 0 #rightside player 1
P2G = 0 #leftside player 2
#player 1
P11 = 4
P12 = 4
P13 = 4 
P14 = 4
P15 = 4
P16 = 4 
#player 2 
P21 = 4
P22 = 4
P23 = 4
P24 = 4
P25 = 4
P26 = 4
def PrintGrid():
    print(f"P2 || {P21} || {P22} || {P23} || {P24} || {P25} || {P26} || ")
    print(f" {P2G} ================================ {P2G}")
    print(f"   || {P21} || {P22} || {P23} || {P24} || {P25} || {P26} || P1")
PrintGrid()
Turn = True 
while Turn:
    print 
