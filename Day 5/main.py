users=[
    {'username':'admin', 'password': 'admin002'},
    {'username':'ram', 'password': 'ram002'},
    {'username':'sita', 'password': 'sita002'},
]

username=input("Enter Username:")
password=input("Enter password:")

login= False
for user in users:
    if user['username']==username and user['password']==password:
        login= True

if login:
    print(f"Welcome {username}")
else:
    print("Ivalid username or password")