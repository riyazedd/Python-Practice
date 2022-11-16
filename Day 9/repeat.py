list=[1,2,1,1,2,3,4,5]
rep=[]
for i in range(len(list)):
    a=i+1
    for j in range(a,len(list)):
        if list[i]==list[j] and list[j] not in rep:
            rep.append(list[j])
print("repeated numbers=",rep)

for x in rep:
    print(f"number of repetition of {x}={list.count(x)}")