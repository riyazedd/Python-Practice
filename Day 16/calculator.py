from operations import add,sub,mul,div #operations bata import gareko

print("Operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Dvision")

opt=int(input("Enter Your Operation: "))

if opt<=4: #if operations choice 4 samma vayo vane matra execute hunxa
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    def calculator():
        if opt==1:
            return add(a,b)
        elif opt==2:
            return sub(a,b)
        elif opt==3:
            return mul(a,b)
        else:
            return div(a,b)
    print(f"Result= {calculator()}")

else:
    print("Enter Valid Operation")