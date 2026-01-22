# Write a Python program to display Pascal's Triangle of n rows
n = int(input("Enter the number of rows : "))
for i in range(1, n + 1):
    C = 1
    for j in range(1, i + 1):
        print(C, " ", end=" ")
        C = C * (i - j) // j
    print()
