from operations import add,sub,mul,div

print("Operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Dvision")

opt=int(input("Enter your choice: "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def calculator():
    if opt==1:
        return add(a,b)
    elif opt==2:
        return sub(a,b)
    elif opt==3:
        return mul(a,b)
    elif opt==4:
        return div(a,b)
    else:
        return ("Choose valid option.")

print(f"Result= {calculator()}")

