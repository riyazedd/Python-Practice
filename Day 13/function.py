# def my_function(): #def le function lai define garxa ani body ma code lekhinxa
#     print("hello world!!!")

# my_function() #function call gareko


# def user():
#     name="Riyaz"
#     age=19
#     return [name,age]

# print(f"My name is {user()[0]}. I am {user()[1]} years old.")

# p=int(input("Enter principle= "))
# t=int(input("Enter time= "))
# r=int(input("Enter rate= "))
# def interest(p,t,r):
#     return p*t*r/100

# print(f"Interest= {interest(p,t,r)}")

def take_value():
    p=int(input("Enter principle= "))
    t=int(input("Enter time= "))
    r=int(input("Enter rate= "))
    return [p,t,r]

def calculator():
    sp=take_value()
    return sp[0]*sp[1]*sp[2]/100

def display():
    print(f"Simple Interest= {calculator()}")

display()