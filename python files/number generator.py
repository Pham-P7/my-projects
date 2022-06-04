#encription key
import random
def placeFinder():
    global AOrder
    global BOrder
    global COrder
    print(f"the sum of these 3 numbers is {a+b+c}")
    print(f"The product of these 3 numbers is {a*b*c}")
    if a > b and a > c:
        AOrder = "highest"
    elif (a > b and a < c) or (a > c and a < b):
        AOrder = "middle"
    else:
        AOrder = "lowest"
    if b > a and b > c:
        BOrder = "highest"
    elif (b > a and b < c) or (b > c and b < a):
        BOrder = "middle"
    else:
        BOrder = "lowest"
    if c > a and c > b:
        COrder = "highest"
    elif (c > a and c < b) or (c > b and c < a):
        COrder = "middle"
    else:
        COrder = "lowest"
    print(f"Enter the password numbers in order {AOrder}, {BOrder}, {COrder}")
    if (a == b) or (a == c) or (b == c):
        print("there is a duplicate number")
def EnterDigits():
    global game
    global level
    global strikes
    while game == True:
        FirstDigit = int(input("What is the first number?: "))
        if FirstDigit != a:
            strikes += 1
            print(f"thats a strike you have {3 - strikes} strikes left")
        if FirstDigit == a:
            print("correct")
            SecondDigit = int(input("what is the second number?: "))
            if SecondDigit != b:
                strikes += 1
                print(f"thats a strike you have {3 - strikes} strikes left")
            if SecondDigit == b:
                print("correct")
                ThirdDigit = int(input("what is the third number?: "))
                if ThirdDigit != c:
                    strikes += 1
                    print(f"thats a strike you have {3 - strikes} strikes left")
                if ThirdDigit == c:
                    print("you have finished the level")
                    level = level + 1
                    strikes = 0
        if strikes == 3:
            print("you have failed")
            print(f"the password was {a} {b} {c}")
            game = input("if you wish to play again enter 'play again' else enter quit: ")
            if input == "play again":
                game = True
                level = 1
            else:
                game = False
game = True
strikes = 0
level = 1
while game == True:
    a = random.randint(1,(6 + 5*(level - 1)))
    b = random.randint(1,(6 + 5*(level - 1)))
    c = random.randint(1,(6 + 5*(level - 1)))
    print(f"level {level}")
    placeFinder()
    EnterDigits()
if game == False:
    print(f"you have completed {level - 1} levels")