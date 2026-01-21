"""Wite a Python program to merge two Python Dictionaries,
sum all the items in the merged Dictionary and print the Dictionary in the table format"""
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 15, 'b': 25, 'd': 35, 'e': 45}
print("Dictionary - 1\n", dict1)
print("Dictionary - 2\n", dict2)
dict3 = dict1
dict3.update(dict2)  # Merge the two dictionaries into dict3
print("The Merged Dictionary")
print("Dictionary - 3\n", dict3)
# sum the values of the dict3
sum = 0
for i in dict3.values():
    sum = sum + i
print("The sum of the dictionary values is :", sum)
newlist = dict3.items()  # list of tuple of key-value pair
print("Key", "Value")
# print the values of dict3 in a table format
for i, j in dict3.items():
    print(i, "   ", j)
