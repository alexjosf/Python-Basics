# Write a Python program to demonstrate exception handling
# This code checks whether the person is eligible to cast vote in India after accepting age and citizenship details
try:
    name = str(input('Enter the name : '))
    age = int(input('Enter the age : '))
    citizen = str(input('Are you a citizen of India - y/n : '))
    if age < 18 or citizen == 'n':
        raise ValueError(name)
except ValueError:
    print(name, " is not eligible to vote in India")
else:
    print("Eligible to vote in India")
finally:
    print("Reached the end of the code")
