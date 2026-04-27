#Len is an example of a polymorphism function.
# mystring="Welcome"
# print(len(mystring))

# mylist=[10,20,30,40,50]
# print(len(mylist))

# mytuple=(1,2,3,4,5)
# print(len(mytuple))

# mydic={"id":123,"name":"John"}
# print(len(mydic))


#Example of method overloading(polymorphism)
# class Human:
#     def sayHello(self,name=None):
#         if name!=None:
#             print("Hello "+name)
#         else:
#             print("Hello")    
# h=Human()
# h.sayHello("John")
# h.sayHello()


class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal=Calculation()
cal.add()
cal.add(10,20)
cal.add(10,20,30)