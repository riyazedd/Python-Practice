username= input("Enter username:")
password= input("Enter password:")

# if username=='admin' and password=='admin002':
#     print("Login Sucessful")

# else:
#     if username != 'admin':
#         print("Username not match...")
#     elif password != 'admin002':
#         print("Password not match...")
#     else:
#         print("Password and match")
if username == 'admin':
    if password == 'admin002':
        print(f"Welcome {username}")
    else:
        print("Invalid Password")
else:
    print("Username not found.")