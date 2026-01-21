# Write a Python program to check whether a number is perfect square
import math

n = int(input("Enter the number : "))
x = math.sqrt(n)
y = int(x)
if n == y * y:
    print(n, " is a perfect square ")
else:
    print(n, " is not a perfect square")
