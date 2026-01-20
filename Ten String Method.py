# Write a Python program to implement atleast ten string methods.
choice = """
String Methods in Python
1 - Length of a string
2 - Slicing a string
3 - Concatenate two strings
4 - Capitalize the first character of a string
5 - Convert all the characters in a string to lowercase
6 - Convert all the characters in a string to uppercase
7 - Convert case of characters in a given string
8 - Count the number of occurence of a character or a string 
9 - Check whether a string starts with a particular character
10 - Check whether a string ends with a particular character
"""


def stringinput():
    sinput = input("Enter the string : ")
    return sinput


print(choice)
option = int(input("Enter the choice : "))
if option == 1:
    s = stringinput()
    print("Length of the string ", s, " is ", len(s))
elif option == 2:
    s = stringinput()
    start = int(input("Enter starting position : "))
    end = int(input("Enter ending position : "))
    print(s[start - 1:end], " is the sliced string from ", s)
elif option == 3:
    print("First String")
    s1 = stringinput()
    print("Second String")
    s2 = stringinput()
    print("The concatenated string is ", s1 + s2)
elif option == 4:
    s = stringinput()
    print("Capitalised string \n", s.capitalize())
elif option == 5:
    s = stringinput()
    print("Lowercase String \n", s.lower())
elif option == 6:
    s = stringinput()
    print("Uppercase String \n", s.upper())
elif option == 7:
    s = stringinput()
    print("Uppercase String \n", s.swapcase())
elif option == 8:
    s1 = stringinput()
    s2 = input("Enter the substring : ")
    print("The number of occurrence of ", s2, " in ", s1, " is ", s1.count(s2))
elif option == 9:
    s1 = stringinput()
    s2 = input("Enter the character : ")
    if s1.startswith(s2):
        print(s1, " starts with the letter ", s2)
    else:
        print(s1, " does not starts with the letter ", s2)
elif option == 10:
    s1 = stringinput()
    s2 = input("Enter the character : ")
    if s1.endswith(s2):
        print(s1, " ends with the letter ", s2)
    else:
        print(s1, " does not ends with the letter ", s2)
