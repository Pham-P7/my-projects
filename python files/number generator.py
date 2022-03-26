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
    FirstDigit = input("What is the first number?")
    if FirstDigit == a:
        print("correct")
        SecondDigit = input("what is the second number?")
        if SecondDigit == b:
            print("correct")
            ThirdDigit = input("what is the third number?")
            if ThirdDigit == c:
                print("you have finished the level")
                level += 1
    else:
        print("you have failed")
        game = input("if you wish to play again enter 'play again' else enter quit")
        if input == "play again":
            game = 0
            level = 1
        else:
            game = 1
game = 0
while game == 0:
    level = 1
    if level == 1:
        a = random.randint(0,6)
        b = random.randint(0,6)
        c = random.randint(0,6)
        print("level 1")
        placeFinder()
        EnterDigits()
    if level == 2:
        a = random.randint(0,11)
        b = random.randint(0,11)
        c = random.randint(0,11)
        print("level 2")
        placeFinder()
        EnterDigits()
    if level == 3:
        a = random.randint(0,31)
        b = random.randint(0,31)
        c = random.randint(0,31)
        print("level 3")
        placeFinder()
        EnterDigits()
    if level == 4:
        a = random.randint(0,101)
        b = random.randint(0,101)
        c = random.randint(0,101)
        print("Welcome to insanity")
        placeFinder()
        EnterDigits()
    if level == 5:
        game = 2
if game == 2:
    print("congrats you have won")
elif game == 1:
    print("you have given up")