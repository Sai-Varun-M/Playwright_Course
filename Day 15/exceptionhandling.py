#Handling exceptions using try and except
# print("Started")
# try:
#     print(x)
# except:
#     print("An exception occured")
# print("Finished")


# print("Started")
# try:
#     print(x)
# except ValueError:
#     print("Variable x is not defined.")
# except:
#     print("Some Other exception")
# print("Finished")


# Else with Try
# try:
#     # print("Hello")
#     100/0
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")


#Finally 
# try:
#     # print(x)
#     print("Welcome")
# except:
#     print("something went wrong")
# finally:
#     print("Try except is finished")


# try:
#     n=int(input("Enter a value: "))
#     res=100/n
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Enter a valid number")
# else:
#     print(res)
# finally:
#     print("Exceptions completed")


#Try within Try
# try:
#     file=open("/Users/saivarun/Documents/Playwright_Course/Day 15/exampfile.txt","w")
#     try:
#         file.write("Welcome")
#     except:
#         print("Something went wrong when writing data into file")
#     finally:
#         file.close()
# except:
#     print("Something went wrong with opening the file")
# else:
#     print("Text written into the file")


#Raise exception
# x=-1
# if x<0:
#     raise Exception("Sorry, no numbers below zero")


# x="Hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")


def set(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    print("Age is set", age)

try:
    set(-20)
except Exception as e:
    print(e)
finally:
    print("Finished running the code")