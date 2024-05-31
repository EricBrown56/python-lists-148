# Python lists

# Lists are a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way.

# lists are a collection of items, mutable, ordered, and have dynamic sizing

#-- ordered : each element in a list has a fixed position
#-- mutable : elements can be changed
#-- dynamic sizing : size of a list can be changed

# creating a list : use square brackets [], and separate items with commas

# empty list

empty_list = []

# populate a list

person = 'Jill'

people = ['Bob', 'Barry', 'Bernie', 'Bill', person]

# Python lists can contain a variety of data types

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis', ['tacos']]]
         
#----- LIst Indecies

# ach item is marked by specific index
# indices are in numerical order, starting at 0, we can use indecies to access, movify, and remove items from a list

# indicies  0        1        2        3
alist = ['item1', 'item2', 'item3', 'item4']
print(alist)

# grab item 3 with index 2

print("Third item: ", alist[2])

# grab item 1 with index 0

print("First item: ", alist[0])

# grab last item with index 3

print("Last item: ", alist[3])

# grab last item with index -1

print("Last item: ", alist[-1])

# potential index errors

# print(alist[4]) # IndexError: list index out of range

# print(alist[-5]) # IndexError: list index out of range












