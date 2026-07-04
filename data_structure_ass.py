# Practical Questions

# Ques1. Write a code to create a string with your name and print it.

name = "Sahil"
print(name)

# Ques2. Write a code to find the length of the string "Hello World".

print(len("Hello World"))

# Ques3. Write a code to slice the first 3 characters from the string "Python Programming".

str = "Python Programming"
print(str[:3])

# Ques4. Write a code to convert the string "hello" to uppercase.

str = "hello"
print(str.upper())

# Ques5. Write a code to replace the word "apple" with "orange" in the string "I like apple".

a = "I like apple"
print(a.replace("apple", "orange"))

# Ques6. Write a code to create a list with numbers 1 to 5 and print it.

a = [i for i in range(1,6)]
print(a)

# Ques7. Write a code to append the number 10 to the list [1, 2, 3, 4].

lst = [1, 2, 3, 4]
lst.append(10)
print(lst)

# Ques8. Write a code to remove the number 3 from the list [1, 2, 3, 4, 5].

lst = [1, 2, 3, 4, 5]
lst.remove(3)
print(lst)

# Ques9. Write a code to access the second element in the list ['a', 'b', 'c', 'd'].

lst = ['a', 'b', 'c', 'd']
print(lst[1])

# Ques10. Write a code to reverse the list [10, 20, 30, 40, 50].

lst = [10, 20, 30, 40, 50]
lst.reverse()
print(lst)

# Ques11. Write a code to create a tuple with the elements 100, 200, 300 and print it.

tup = (100, 200, 300)
print(tup)

# Ques12. Write a code to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow').

tup = ('red', 'green', 'blue', 'yellow')
print(tup[-2])

# Ques13. Write a code to find the minimum number in the tuple (10, 20, 5, 15).

tup = (10, 20, 5, 15)
print(min(tup))

# Ques14. Write a code to find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit').

tup = ('dog', 'cat', 'rabbit')
print(tup.index("cat"))

# Ques15. Write a code to create a tuple containing three different fruits and check if "kiwi" is in it.

fruits = ("mango", "banana", "apple")
print("kiwi" in fruits)

# Ques16. Write a code to create a set with the elements 'a', 'b', 'c' and print it.

sets = {'a', 'b', 'c'}
print(sets)

# Ques17. Write a code to clear all elements from the set {1, 2, 3, 4, 5}.

sets = {1, 2, 3, 4, 5}
sets.clear()
print(sets)

# Ques18. Write a code to remove the element 4 from the set {1, 2, 3, 4}.

sets = {1, 2, 3, 4}
sets.remove(4)
print(sets)

# Ques19. Write a code to find the union of two sets {1, 2, 3} and {3, 4, 5}.

sets1 = {1, 2, 3}
sets2 = {3, 4, 5}

print(sets1.union(sets2))

# Ques20. Write a code to find the intersection of two sets {1, 2, 3} and {2, 3, 4}.

sets1 = {1, 2, 3}
sets2 = {2, 3, 4}

print(sets1.intersection(sets2))

# Ques21. Write a code to create a dictionary with the keys "name", "age", and "city", and print it.

dict = {"name" : "Sahil Kumar",
        "age" : 23, 
        "city" : "Prayagraj"}

print(dict)

# Ques22. Write a code to add a new key-value pair "country": "USA" to the dictionary {'name': 'John', 'age': 25}.

dict = {'name': 'John', 'age': 25}
dict['country'] = "USA"
print(dict)

# Ques23. Write a code to access the value associated with the key "name" in the dictionary {'name': 'Alice', 'age': 30}.

dict = {'name': 'Alice', 'age': 30}
print(dict['name'])


# Ques24. Write a code to remove the key "age" from the dictionary {'name': 'Bob', 'age': 22, 'city': 'New York'}.

dict = {'name': 'Bob', 'age': 22, 'city': 'New York'}
del dict['age']
print(dict)

# Ques25. Write a code to check if the key "city" exists in the dictionary {'name': 'Alice', 'city': 'Paris'}.

dict = {'name': 'Alice', 'city': 'Paris'}
print("city" in dict)

# Ques26.  Write a code to create a list, a tuple, and a dictionary, and print them all.

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}
print(my_list)
print(my_tuple)
print(my_dict)

# Ques27. Write a code to create a list of 5 random numbers between 1 and 100, sort it in ascending order, and print the
# result.(replaced)

import random 
lst = random.sample(range(1, 100), 5)
lst.sort()
print(lst)

# Ques28. Write a code to create a list with strings and print the element at the third index.

lst = ["apple", "mango", "gauva", "strawberry", "watermelon"]
print(lst[3])

# Ques29. Write a code to combine two dictionaries into one and print the result.

d1 = {"name": "Alice", "age": 25}
d2 = {"city": "Paris", "country": "France"}

# combined = {**d1, **d2} modern way to combine dictionaries
print({**d1, **d2})

# Ques30. Write a code to convert a list of strings into a set.

lst1 = ["s", "a", "h", "i", "l", "k", "u", "m", "a", "r"]
s = set(lst1)
print(s)