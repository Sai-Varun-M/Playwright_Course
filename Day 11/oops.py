#Creating a class along with object
# class Myclass:
#     def myfunc(self):
#         pass

#     def display(self,name):
#         print(name)

# mc1=Myclass()
# mc1.myfunc()
# mc1.display("Sai")

# mc2=Myclass()
# mc2.myfunc()
# mc2.display("Varun")


#Instance method vs static method
# class Myclass:
#     def m1(self):
#         print("This is instance method")
    
#     @staticmethod
#     def m2(self,num):
#         print(num)

# mc= Myclass()
# mc.m1()
# mc.m2(10,2)


#Define variable inside the class
# class Myclass:
#     a,b=10,20

#     def add(self):
#         print(self.a+self.b)
    
#     def mul(self):
#         print(self.a*self.b)
    
# m1=Myclass()
# m1.add()
# m1.mul()


#Local variable, Global variables and class variables
# i,j=15,25 #Global Variables

# class Myclass:
#     a,b=10,20 #Class varaibles
#     def add(self,x,y):
#         print(x+y) #Local varaibles
#         print(self.a+self.b) #Class variables
#         print(i+j) #Global variables 

# mc=Myclass()
# mc.add(100,200)


#Constructor
# class Myclass:
#     def __init__(self):
#         print("This is constructor...")
#     def m1(self):
#         print("Hello...")
#     def add(self,x,y):
#         print(x+y)

# m1=Myclass()
# m1.add(2,3)


#Constructor with parameter
# class Myclass():
#     name="John"

#     def __init__(self,name):
#         print(name) #David
#         print(self.name) #John

# mc=Myclass("David")


#Class with constructor and method
class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print(self.eid,self.ename,self.sal)

e1=Emp(101,"John",500000)
e1.display()