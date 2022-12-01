# def all_students():
#     return "All Students"

data=[
    {'name':'ram','address':'kathmandu','age':20},
    {'name':'hari','address':'bhaktapur','age':30},
    {'name':'ram','address':'lalitpur','age':25},
]

def get_students():
    return data

def get_students(name):
    for i in data:
        if i['name']==name:
            print(i)

get_students('ram')