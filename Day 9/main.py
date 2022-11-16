# defining total number of integers
num=int(input("Enter the total number= "))
count=1
data=[]
#taking input integers and adding in list
while count<=num:
    number=int(input(f"Enter {count} number= "))
    data.append(number)
    count +=1
#finding the repeated numbers
rep=[]
for x in data:
    if data.count(x)>1 and x not in rep:
        rep.append(x)
print("Repeated numbers= ",rep)
#finding the total repetition of each repeated numbers
for x in rep:
    print(f"Number of repetition of {x}= {data.count(x)}")
