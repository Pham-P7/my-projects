import random
level = 1
if level == 1:
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    print(a,b,c)
    print(f"the sum of these 3 numbers is {a+b+c}")
    print(f"The product of these 3 numbers is {a*b*c}")
    if a > b and a > c:
        AOrder = "greatest"
    elif (a > b and a < c) or (a > c and a < b):
        AOrder = "middle"
    else:
        AOrder = "least"
    if b > a and b > c:
        BOrder = "greatest"
    elif (b > a and b < c) or (B)
    if c > a and c > b:
        Corder = "greatest"
    list = [a,b,c]