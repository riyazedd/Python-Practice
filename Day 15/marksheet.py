def take_marks():
    # marks=[]
    nep=int(input("Enter marks of Nepali= "))
    eng=int(input("Enter marks of English= "))
    mth=int(input("Enter marks of Math= "))
    sci=int(input("Enter marks of SCience= "))
    acc=int(input("Enter marks of Account= "))
    subject=[nep,eng,mth,sci,acc]
    # marks.append(subject)
    return subject

def total():
    return sum(take_marks())

def percentage():
    sum=total()
    per=sum/5
    return per
    
def display():
    take_marks()
    print(total())
    print(percentage())

display()