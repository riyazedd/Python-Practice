#---------------loop-------------
# data=[
#     [1,2,3,4,5,6,7,8,9],
#     [10,11,12,13,14,15],
#     [16,17,18,19,20,21],
# ]

# for x in data:
#     for y in x:
#         print(y)

num1=int(input("Enter first number= "))
num2=int(input("Enter second number= "))
num3=int(input("Enter third number= "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num1,num2,num3)
    else:
        print(num1,num2,num3)
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
else:
    if num1>num2:
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)
