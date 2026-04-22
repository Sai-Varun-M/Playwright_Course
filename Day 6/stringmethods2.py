# print("123".isdecimal()) #True
# print("10.5".isdecimal()) #False (dont doesn't come under deciaml number system)

# print("123".isdigit())
# print("10.5".isdecimal())


# print("123".isnumeric())
# print("10.5".isnumeric())


#Splitting Strings
# s="abc@gmail.com"
# l=s=s.split("@")
# print(type(l))
# print(l)
# print(l[0])
# print(l[1])


# s="one,two,three"
# lst=s.split(",")
# print(lst)
# print(lst[2])


# s="welcome"
# print(s.startswith("wel")) #True
# print(s.startswith("Wel")) #False
# print(s.endswith("come")) #True
# print(s.endswith("Come")) #False


# Trimming Spaces in Strings
s= "   hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())