# Write a Python program to demonstrate different types of inheritance
# Single Inheritance
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')


# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Create object of Car
obj = Car()

# access Vehicle's info using car object
obj.Vehicle_info()
obj.car_info()


# %%
# Multiple Inheritance
# Parent class 1
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# Parent class 2
class Company:
    def __init__(self, companyname):
        self.companyname = companyname


# Child class
class Employee(Person, Company):
    def __init__(self, name, age, salary, companyname, skill):
        Person.__init__(self, name, age, salary)
        Company.__init__(self, companyname)
        self.skill = skill
        print(name, ' works for ', companyname, 'for a salary of $', salary, ' in the ', skill, 'domain')


# Create object of Employee
emp = Employee('John', 28, 3000, 'Google', 'Machine Learning')


# %%
# Multilevel Inheritance
class Animal:
    def description(self):
        print("Animals got For Legs.")
    # The child class Dog inherits the base class Animal


class Dog(Animal):
    def sound(self):
        print("Dogs is an animal which makes barking sound and are carnivoros.")
    # The child class Dogchild inherits another child class Dog


class DogChild(Dog):
    def name(self):
        print("The baby of a dog is called a Puppy.")


d = DogChild()
d.description()
d.sound()
d.name()
