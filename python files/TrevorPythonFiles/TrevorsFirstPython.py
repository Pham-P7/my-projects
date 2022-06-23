# we use no header files because it already knows what "print" is
# many ways for same outcome
# main function is not needed in python
print("Hello, World")
print("Hello, \
World")
print("Hello, " + "World")
# we don't use "int" or "string" to say what type of data the variable will be
x = "Hello, World"
# special formating ways to print a variable
print(x)
print("%s" %(x))
print(f"{x}")

y = "Hello, "
x = "World"
# concatination of strings plus variable
print(y  + x)
# below are strings plus variable and we can flip it to work for y and not x
print("Hello,", x)
print("Hello, " + x)
print(f"Hello, {x}")
print(str.format("Hello, {0}", "world"))
print(str.format("Hello, {0}", x))
print("Hello, %s" %(x))
# ; is also not needed ever in python at the end of each line of code
# at the bottom is another way of printing usign a list but i could format this is so many other ways 
# im just too lazy
list = ["H","e","l","l","o",","," ","W","o","r","l","d"]
for i in range(len(list)):
    print(list[i], end = "")