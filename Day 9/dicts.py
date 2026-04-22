#Creating a dictionary
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# print(dict)
# dict2=dict(name="john",age = 35, country = "india")
# print(dict2)


# A key can have multiple values
# dict1={
#     "brand":"Ford",
#     "model": "Aspire",
#     "year": 2024,
#     "color":["red",'white','blue']
# }
# print(dict1)


#Accessing items from dictionary
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# print(dict1["model"])


#Get keys
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# print(dict1.keys())


#Get values
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# print(dict1.values())


#Keys cannot be duplicated but values can be duplicated.


#Get items
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# print(dict1.items()) #Prints in tuple format


#Check if a key already exists
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# if "model" in dict1:
#     print("Exists")
# else:
#     print("Not Exists")


#Adding items to dictionary
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# dict1["color"]="red"
# print(dict1)


#Updating a dictionary
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# dict1["color"]="red"
# dict1.update({"year":2025})
# dict1.update({"color":"blue"})
# print(dict1)


#Removing items from a dictionary
# dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
# dict1.pop("year")
# print(dict1)

dict1 = {"brand":"Ford", "model":"Aspire","year":2004}
dict1.popitem()
print(dict1)