def my_reps(data,times):
    rep=1
    while rep<=times:
        print(data)
        rep+=1
my_reps('riyaz',5)

def my_reps(data,times):
    return str(data)*times

print(my_reps('riyaz',5))