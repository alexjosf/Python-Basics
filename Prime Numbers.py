# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.(use list
# class).
import math

n = int(input("Enter the number : "))
prime = []
for i in range(2, n + 1):  # creating a list of numbers from 0 to n
    prime.append(i)
i = 2
while i <= int(math.sqrt(n)):
    if i in prime:  # if i is in prime delete its multiples
        for j in range(i * 2, n + 1, i):  # j will give multiples of i starting from 2*i
            if j in prime:
                prime.remove(j)  # delete the multiple if found in list
    i = i + 1
print(" Prime numbers up to ", n, "\n", prime)
