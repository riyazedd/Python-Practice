num= int(input("Enter number of students: "))
x=1

students_marks=[]
while x<=num:
    print(f"=====================Student:{x}=======================")
    for subject in range(1):
        nepali= int(input("Enter marks of Nepali: "))
        english= int(input("Enter marks of English: "))
        math= int(input("Enter marks of Math: "))
        social= int(input("Enter marks of Social: "))
        science= int(input("Enter marks of Science: "))
        all_subject= [nepali,english,math,social,science]
        students_marks.append(all_subject)
    x +=1

for student in students_marks:
    total=0
    for marks in student:
        total += marks
    
    percentage= total/5

    print(f"Total marks= {total}\nPercentage= {percentage}")
    if percentage>=80:
        print(f"Division: A with {percentage}")
    elif percentage>=70:
        print(f"Division= B with {percentage}")
    elif percentage>=60:
        print(f"Division= C with {percentage}")
    elif percentage>=50:
        print(f"Division= D with {percentage}")
    elif percentage>=40:
        print(f"Division= E with {percentage}")
    else:
        print(f"Division= Fail with {percentage}")
