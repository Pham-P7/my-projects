import random
def placeFinder():
    global AOrder
    global BOrder
    global COrder
    print(f"the sum of these 3 numbers is {a+b+c}")
    print(f"The product of these 3 numbers is {a*b*c}")
    if a > b and a > c:
        AOrder = "first"
    elif (a > b and a < c) or (a > c and a < b):
        AOrder = "middle"
    else:
        AOrder = "last"
    if b > a and b > c:
        BOrder = "first"
    elif (b > a and b < c) or (b > c and b < a):
        BOrder = "middle"
    else:
        BOrder = "last"
    if c > a and c > b:
        COrder = "first"
    elif (c > a and c < b) or (c > b and c < a):
        COrder = "middle"
    else:
        COrder = "last"
level = 1
if level == 1:
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    print(a,b,c)

    list = [a,b,c]