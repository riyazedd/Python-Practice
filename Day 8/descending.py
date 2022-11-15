num1=int(input("Enter first number= "))
num2=int(input("Enter second number= "))
num3=int(input("Enter third number= "))

if num1>num2 and num1>num3:
    if num2>num3:
        pass
    else:
        num1,num2,num3=num1,num3,num2
elif num2>num1 and num2>num3:
    if num1>num3:
        num1,num2,num3=num2,num1,num3
    else:
        num1,num2,num3=num2,num3,num1
else:
    if num1>num2:
        num1,num2,num3=num3,num1,num2
    else:
        num1,num2,num3=num3,num2,num1

print("Numbers in descending order= ",num1,num2,num3)