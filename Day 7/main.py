# data=('ram','sita','hari')
# print(type(data))
# data=list(('ram','sita','hari'))
# print(type(data))
# data.append('kalpana')
# data=tuple(data)
# print(data)
# print(type(data))

# students={
#     "name":"sophia",
#     "address":{
#         "province":{
#             "name":"kathmandu",
#         }
#     }
# }

# print(students["address"]["province"]["name"])


# data = [
#     {'name':'ram', 'gender': 'male', 'status': True},
#     {'name': 'sita', 'gender': 'female', 'status': False},
#     {'name': 'sophia', 'gender': 'female', 'status': True},
#     {'name': 'laxmi', 'gender': 'male', 'status': False},
#     {'name': 'laxmi', 'gender': 'female', 'status': False},
#     {'name': 'gopal', 'gender': 'male', 'status': True},
# ]
# count=0
# for user in data:
#     if user["name"]=="laxmi":
#         count +=1
    
# print("Number of laxmi=",count)

# num=int(input("Enter the number of users= "))
# name=1
# users=[]
# while name<=num:
#     # for x in range(1):
#     username=input("Enter your username: ")
#     users.append(username)
#     name +=1
# print(users)

##
data=[1,2,3,4,5,6,7,8,9,10,3,7,9,9]
rep=[]
for x in data:
    if data.count(x)>1 and x not in rep:
        rep.append(x)
print(rep)