#---------------loop-------------
# data=[
#     [1,2,3,4,5,6,7,8,9],
#     [10,11,12,13,14,15],
#     [16,17,18,19,20,21],
# ]

# for x in data:
#     for y in x:
#         print(y)

x=int(input("Enter first number= "))
y=int(input("Enter second number= "))
z=int(input("Enter third number= "))

# if num1>num2 and num1>num3:
#     if num2>num3:
#         print(num1,num2,num3)
#     else:
#         print(num1,num2,num3)
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print(num2,num1,num3)
#     else:
#         print(num2,num3,num1)
# else:
#     if num1>num2:
#         print(num3,num1,num2)
#     else:
#         print(num3,num2,num1)

if x>y and x>z:
    if y>z:
        x,y,z=x,y,z
    else:
        x,y,z=x,z,y
elif y>x and y>z:
    if x>z:
        x,y,z=y,x,z
    else:
        x,y,z=y,z,x
else:
    if x>y:
        x,y,z=z,x,y
    else:
        x,y,z=z,y,x

print(x,y,z)
