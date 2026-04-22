# Creating String
# name ="John"
# grade = "B"
# name = 'Johan'
# grade = 'NB'
# name = str() #empty string
# grade = str()
# print("First Print:- ",name,grade)
# name = str("John")
# grade = str("B")
# print("Second Print:- ",name,grade)
# print(type(name))
# print(type(grade))

# + and * with strings
# str="welcome "
# print(str+"Programming")
# print(str*3)

#Slicing Strings
# mystr="Welcome"
# print(mystr[1:3]) #el
# print(mystr[:6]) #Welcom
# print(mystr[2:]) #lcome
# print(mystr[1:-1]) #elcom
# print(mystr[1:-2]) #elco
# print(mystr[-5:-2]) #lco

#Formatting Strings
# age=30
# str=f"My name is John, I am {age}"
# print(str)
# print(f"I am John, I am {age}")

# price =55
# str = f"The price is {price:.2f}"
# print(str)

# price =55
# str = f"The price is {price*10}"
# print(str)

#in and not in - returns boolean values
str = "Welcome"
print("come" in str) #True
print("Come" in str) #False
print("Come" not in str) #True
