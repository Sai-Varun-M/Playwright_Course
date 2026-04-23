#Function with arbitary arguments
# def sum_function(*numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     return total

# print(sum_function(10,20))
# print(sum_function(10,20,30))
# print(sum_function(10,20,30,40))
# print(sum_function())


#Function with positional and keyword arguments
def myfun(i,j):
    print(i,j)
myfun(10,20) #positional arguments

myfun(j=20,i=10) #keyword arguments
