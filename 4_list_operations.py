# Other cool things we can do with lists

# Membership check with 'in' to check if an item is in a list, returns a boolean

guest_list = ['Bob', 'Barry', 'Bernie', 'Bill', 'Jill']

print('Bob' in guest_list) # True
print('Brian' in guest_list) # False

#name = input('What is your name?')

guest_list.append('Brian')

# using if statements for membership check

#if name in guest_list:
    #print('Welcome to the party!', name)
#else:
   # print('Sorry, you are not on the list. Goodbye.', name)

# Merging lists with the + operator

list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)

# Copying lists with the .copy() method

# Changes we make to a true copy do not affect the original list

fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit.copy()
print(copy_fruit)

copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

# Copying a list with a full slice list[:]
# Changes we make to a true copy do not affect the original list

fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit[:]
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

# Common mistakes when copying a list is setting one list equal to another

nums = [1,2,3,4]
dums = nums
dums.pop()
print("dums: ", dums)
print("nums: ", nums)

# This is not a true copy, changes to dums will affect nums
#---------------------------------------------------------------------------------------
# Identity operators are 'is' and 'is not' and will return a boolean
# 'is' checks if two variables are the same object

fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit[:]
print(fruit is copy_fruit) # False, does not point to the same object

print(fruit == copy_fruit) # True because the values are the same

nums = [1,2,3,4]
dums = nums
print(nums is dums) # True, points to the same object in memory

# list slicing
# list[start:stop:] : start is the index to start at, stop is the index to stop at. The stop index is not included in the slice. start creates a new list from the start index to the end of the list. stop creates a new list from the beginning of the list to the stop index. The default step is 1, which means that every item in the list will be included in the slice. The default start is 0, the default stop is the end of the list, and the default step is 1.
# default start is 0, default stop is the end of the list

key_lime_pie = ['slice1', 'slice2', 'slice3', 'slice4']
my_slice = key_lime_pie[0:1]
print(my_slice)

big_slice = key_lime_pie[1:3]
print(big_slice)

last_slice = key_lime_pie[3:]
print(last_slice)

last_slice2 = key_lime_pie[-1:]
print(last_slice2)

# By indicating our start value at a negative intex and not specifying an end value we end up including the last item in the list [-2] (also index 2)

# joining lists with the .join() method

# list.join() : join a list of strings into a single string. The method is called on the string that will be used to join the list. The list to be joined is passed as an argument to the method. The method returns a single string.

# ' '.join(list) : join a list of strings with a space between each string

words = ['Hello', 'Im', 'getting', 'joined!']
joined_words = ' '.join(words)
print(joined_words)

new_joined_words = '!!!!!'.join(words)
print(new_joined_words)