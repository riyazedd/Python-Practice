shopping_list=['apple','banana','carrots','papaya','brinjal']

# sorted_list=sorted(shopping_list) #sorts the list in ascending order...reverse=True sorts in decending order
# print(sorted_list)

# shopping_list.sort() #permanently sorts the list

# shopping_list[0]='avacado' #updating or changing the values of list
# print(shopping_list)

# shopping_list[1:4]=['kiwi','lemon','melon'] #multiple items changed
# print(shopping_list)
tim_list=['honey','carrots','coconut']

# shopping_list += tim_list #adding two lists

# shopping_list.append(tim_list) #adds the list by nesting
# shopping_list.extend(tim_list) #adds the items of the list
# shopping_list.insert(1, tim_list) #inserts the list in the mentioned index number
# shopping_list.append('hello') #items can also be appended
# shopping_list.insert(1, "cabbage") #items can be inserted in the mentioned index numeber
print(shopping_list)

to_do_list=['eat','workout','sleep','run','eat','sleep']
print(to_do_list)

# to_do_list.remove('eat') #removes the mentioned item
# to_do_list.pop(1) #remove the item of the mentioned index...no mention of the index removes the last item
removed_item=to_do_list.pop(1) #pop funtion returns the value allowing you to store it in a variable

print(to_do_list)
print(removed_item)