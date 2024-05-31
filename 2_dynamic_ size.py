# Dynamic size means that the size of a list can be changed. This is a powerful feature of Python lists.

bec_class = ['Dillon', 'Christy', 'Tony', 'Eric'] # 4 items
print(bec_class)

# add a student

#------ list.append(item) : add an item to the end of a list

bec_class.append('Cole') # 5 items
print(bec_class)

# add another student

bec_class.append('Jason') # 6 items
print(bec_class)

# add another student

bec_class.append('Jesmarie') # 7 items
print(bec_class)

# add a list of students

bec_class.append(['Jill', 'Jen', 'Jenny']) # 8 items
print(bec_class)

# remove from lists

#------ list.remove(item) : remove an item from a list

bec_class.remove('Jesmarie') # 7 items
print(bec_class)

bec_class.remove(['Jill', 'Jen', 'Jenny']) # 6 items
print(bec_class)

