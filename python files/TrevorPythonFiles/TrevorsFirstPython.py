# we use no header files because it already knows what "print" is
#many ways for same outcome
# function is not needed in python
print("Hello, World")
# we don't use "int" or "string" to say what type of data the variable will be
x = "Hello, World"
print(x)
x = "World"
print("Hello,", x)
print("Hello, " + x)
print(f"Hello, {x}")
print(str.format("Hello, {0}", "world"))
print(str.format("Hello, {0}", x))
print("Hello, %s" %(x))
# ; is also not needed ever in python at the end of each line of code