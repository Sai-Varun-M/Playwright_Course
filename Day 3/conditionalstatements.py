#if
# age = 20
# if age>=18:
#     print("Eligible To Vote")

# amount = 1200
# discount = 0
# if amount >1000:
#     discount=amount*10/100
# print("Actual amount after reducing discount:",amount-discount)

# If else
# age =20
# if age>=18:
#     print("Eligible To Vote")
# else:
#     print("Not Eligible To Vote")

# num =10
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

#if elif else
# amount =1500
# print("Actual Amount:",amount)
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount=amount*10/100
# elif amount>1000:
#     discount=amount*5/100
# else:
#     discount=0
# print("Payment Amount:",amount-discount)

# weekno=1
# if weekno==1:
#     print("Sunday")
# elif weekno==2:
#     print("Monday")
# elif weekno==3:
#     print("Tuesday")
# elif weekno==4:
#     print("Wednesday")
# elif weekno==5:
#     print("Thursday")
# elif weekno==6:
#     print("Friday")
# elif weekno==7:
#     print("Saturday")
# else:
#     print("Invalid Number")

#Nested If
# num=6
# print("Number: ",num)
# if num%2==0:
#     if num%3==0:
#         print("Number is divisible by both 2 and 3")
#     else:
#         print("Number is only divisible by 2")
# elif num%3==0:
#     print("Number is only divisible by 3")
# else:
#     print("Number is not divisible by neither 2 nor 3")

#Short If else
# a,b=20,10
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
# print("a is greater") if a>b else print("b is greater")

#Using logical operators
# a,b,c=30,200,50
# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")

#pass statement
a=10
b=100
if a>b:
    pass
print("something")