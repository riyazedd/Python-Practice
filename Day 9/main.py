num=int(input("Enter the total number= "))
count=1
data=[]

while count<=num:
    number=int(input("Enter a number= "))
    data.append(number)
    count +=1

rep=[]
for x in data:
    if data.count(x)>1 and x not in rep:
        rep.append(x)
print("Repeated numbers= ",rep)

for x in rep:
    print(f"Number of repetition of {x}= {data.count(x)}")
