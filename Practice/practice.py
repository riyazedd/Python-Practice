num1=int(input("Enter first number= "))
num2=int(input("Enter second number= "))

operator=input("Enter your opeation(*,+,-,/)= ")

if operator=='*':
    operation=num1*num2
elif operator=='+':
    operation=num1+num2
elif operator=='-':
    operation=num1-num2
elif operator=='/':
    operation=num1/num2
else:
    print("---OPERATION INVALID---")
    exit()

print(f"Result={operation}")