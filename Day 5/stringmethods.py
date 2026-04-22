#String Methods
# s= "hello"
# print(s)
# print(s.capitalize())
# print(s.upper())
# print(s.lower())


# s= "welcome to python"
# print(s.title())
# a=s.title()
# print(a.swapcase())


# str="banana"
# print(str.center(100))


# s= "hello"
# print(s.find("e")) #1
# print(s.find("l")) #2
# print(s.find("x")) #-1
# print(s.index("e"))
# print(s.index("l"))
# print(s.index("x")) #ValueError


# s="Banana"
# print(s.count("a"))
# print(s.count("na"))


# s="Hello World"
# print(s.replace("World","There"))
# print(s.replace("l","X"))
# print(s)


s="ABC123"
print(s.isalnum()) #True
a="123"
b="abc"
print(a.isalnum()) #True
print(b.isalnum()) #True
print(a.isalpha()) #True
print(b.isalpha) #False
print(b.isdecimal) #True
print(a.isdigit()) #False
print(b.isnumeric()) #True