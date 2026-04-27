# class A:
#     def m1(self):
#         print("This is m1 method from class A")

# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")

# b=B()
# b.m1()
# b.m2()


#Single Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
    
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)

# b=B()
# b.m1()
# b.m2()


#Multi Level Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
    
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)

# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# b=C()
# b.m1()
# b.m2()
# b.m3()


#Hierarchical Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
    
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)

# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# b=B()
# b.m1()
# b.m2()

# c=C()
# c.m1()
# c.m3()


#Mutliple Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
    
# class B():
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)

# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# b=B()
# b.m2()

# c=C()
# c.m1()
# c.m2()
# c.m3()