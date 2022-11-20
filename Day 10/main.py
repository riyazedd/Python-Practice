data={
    "name": "sophia",
    "age": 29,
    # "courses": ['python','java','php','c','c++']
    "phone": 1234567890,
    "address": "kathmandu",
    "contact": [{'phone': 5555, 'mobile': 12345},[{"name": "riyaz"}]]
}
# a=''
# for y in data["courses"]:
#     a+=y + ','
# print(f"My name is {data['name']} and my courses are {a}")

# print(f"My name is {data['name']} and my courses are {', '.join(data['courses'])}")

# data1= ','.join(data['courses'])

# data1=data1.split(',')
# print(data1)

x=data['contact'][1][0]["name"]
print(x)