data = [
    {'name':'ram', 'gender': 'male', 'status': True},
    {'name': 'sita', 'gender': 'female', 'status': False},
    {'name': 'sophia', 'gender': 'female', 'status': True},
    {'name': 'laxmi', 'gender': 'male', 'status': False},
    {'name': 'hari', 'gender': 'female', 'status': False},
    {'name': 'gopal', 'gender': 'male', 'status': True},
]

totalUsers=len(data)
total_male=0
total_female=0
total_active_female=0
total_active_male=0
total_inactive_female=0
total_inactive_male=0

for user in data:
    if user['gender']=='male':
        total_male += 1
    else:
        total_female += 1
        
    if user['status']==True and user['gender']=='male':
        total_active_male += 1
    
    if user['status']==True and user['gender']=='female':
        total_active_female += 1

    if user['status']==False and user['gender']=='male':
        total_inactive_male += 1

    if user['status']==False and user['gender']=='female':
        total_inactive_female += 1


print(f"""Total number of male={total_male}
Total number of female={total_female}
Total Active Male={total_active_male}
Total Active Female={total_active_female}
Total Inactive Male={total_inactive_male}
Total Inactive Female={total_inactive_female}""")