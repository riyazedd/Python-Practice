email=['student@gmail.com','hello@gmail.com','hey@gmail.com']

newEmail=input("Enter new email= ")

# for mail in email:
if newEmail in email:
    print("Your new email is already in use...Try another email")
else:
    print("Your new email is regestered...")