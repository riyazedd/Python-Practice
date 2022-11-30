subjects=['Maths','MicroProcessor','English','C Programming','Account']
marks=[]
def take_marks():
    for i in range(len(subjects)):
        marks.append(int(input(f"Enter the marks of {subjects[i]}: ")))
    return marks
def total():
    return sum(marks)

def percentage():
    per=total()/5
    return per

def grade():
    if percentage()>=80:
        division='A'
        return division
    elif percentage()>=60:
        division='B'
        return division
    elif percentage()>=40:
        division='C'
        return division
    else:
        division='D'
        return division
take_marks()
print("----------RESULT----------")
print(f"Total Marks: {total()}\nPercentage Obtained: {percentage()}\nGrade Obtained: {grade()}")