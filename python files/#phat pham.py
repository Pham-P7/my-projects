#phat pham
validOrders = ("burger","fries","salad","soda","milkshake")
itemDescriptions = ("Half-pound burger","Large fries","Side salad", "Diet root beer", "Chocolate shake")
order = []
print("Welcome to Burger Castle")
print("Menu: ", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")
item = " "
while item != "" or "quit":
    item = input("Enter Item: ")
    if item in validOrders:
        order.append(item)
    elif item != validOrders:
        if(item != ""):
            if(item != "quit"):
                print("Sorry, we don't sell " + item)
            else:
                break
        else:
            break
print()
print("Order complete; you are having:")
for item in order:
    if item in validOrders:
        index = validOrders.index(item)
        description = itemDescriptions[index]
        print(description)
print("Thanks for visiting Burger Castle")