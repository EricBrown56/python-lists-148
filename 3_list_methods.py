# some cool things we can do with list methods

food = ['tacos', 'pizza', 'tiramisu'] 
print(food)

#------ list.append(item) : add an item to the end of a list

food.append('ice cream')
print(food)

#--- list.insert(index, item) : add an item to a specific index in a list

# adding to a list at an index that doesn't exist will add to the end of the list

food.insert(2, 'potato')
print(food)

#------ list.remove(item) : remove an item from a list

food.remove('pizza')
print(food)



#------ list.pop() : remove the last item from a list

freezer = food.pop()
print(food)
print("Freezer: ", freezer)

# just because it returns a value doesnt mean we have to store it in a variable

#------ list.pop(index) : remove an item from a specific index in a list

oven = food.pop(1)
print(food)
print("Oven : ", oven)

# Hit up the grocery store

food.append('burger')
food.append('bread')
food.append('cheese')
food.append('sushi')
food.append('chicken')

print('we went to the store')
print(food)

#---- list.index(item) : find the index of an item in a list

print('Finding the index of bread using list.index(item)')
bread_index = food.index('bread')
print("Bread index: ", bread_index)

#---- Modify the values at a particular index. MUTABILITY list[index] = new_value

print('Changing the value of bread to buns')
food[3] = 'buns'
print(food)

food.append('burger')
print(food)

#---- list.count(item) : count the number of times an item appears in a list it will always return an integer

print('Counting the number of burgers in the list')
burger_count = food.count('burger')
print("Burger count: ", burger_count)

#---- list.reverse() : reverse the order of a list

print('Reversing the list')
food.reverse()
print(food)

#---- list.sort() : sort a list in ascending or alphabetical order. All items must be of the same type

print('Sorting the list')
food.sort()
print(food)

#--- list.sort(reverse = True) : sort a list in descending order

print('Sorting the list in reverse')
food.sort(reverse = True)
print(food)

#------ List functions

#---- len(item) : get the length of a list

print('The length of the list is: ', len(food))

#---- sum(list) : get the sum of a list. List must be made of integers or floats

numbers = [1, 2, 3, 4, 5, 6, 4.4]
total = sum(numbers)
print('The sum of the numbers list is: ', total)

mess = [False, True, False] #Boolean values are treated as 0 and 1
mess.sort()
print(mess)





