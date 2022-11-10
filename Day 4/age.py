age= int(input("Enter your age:"))

if age >= 18:
    if age >= 18 and age <=24:
        print("You can drink Wine only...Enjoy!!!")
    elif age >24 and age <=34:
        print("You can drink Wine and Beer...Enjoy!!!")
    else:
        print("You can drink anything...Enjoy!!!")
else:
    print("You are not allowed in party...Go Home!!!")