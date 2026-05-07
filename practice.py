###Day 1
# Example 1
x = 5
print(x)

# Example 2
name = "Ankit"
print("Hello", name)

# Example 3
for i in range(5):
    print(i)

# Example 4
def add(a, b):
    return a + b

print(add(2, 3))

# Day 2 Practice - Strings, Input, Indexing, Slicing, Type Conversion

# -------------------------------
# 1. String Basics
# -------------------------------
name = "Ankit"
print("Name:", name)
print("Type:", type(name))


# -------------------------------
# 2. Indexing
# -------------------------------
word = "PYTHON"

print("First character:", word[0])
print("Fourth character:", word[3])
print("Last character:", word[-1])
print("Second last:", word[-2])


# -------------------------------
# 3. Slicing
# -------------------------------
text = "Hello"

print("Slice 0:4 ->", text[0:4])
print("First 3 ->", text[:3])
print("From index 3 ->", text[3:])
print("Full copy ->", text[:])


# -------------------------------
# 4. String Methods
# -------------------------------
msg = "   Hello Python   "

print("Upper:", msg.upper())
print("Lower:", msg.lower())
print("Strip:", msg.strip())

sentence = "I like Apple"
print("Replace:", sentence.replace("Apple", "Mango"))

# Method chaining
clean_text = msg.strip().upper()
print("Cleaned:", clean_text)


# -------------------------------
# 5. Reverse String
# -------------------------------
name = "Rahul"
print("Reversed:", name[::-1])


# -------------------------------
# 6. Input and Type Conversion
# -------------------------------
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Wrong (string join)
print("Joined:", num1 + num2)

# Correct (numeric addition)
sum_result = int(num1) + int(num2)
print("Sum:", sum_result)


# -------------------------------
# 7. Extra Thinking Example
# -------------------------------
x = "10"
y = 5

# print(x + y)  # This gives error

print("Fixed:", int(x) + y)



# Day 3 - If Else Practice

# Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
else:
    print("B is greater")



# Day 4 - Loops Practice

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# 2. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 3. Find sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# 4. Print multiplication table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 5. Countdown using while loop
i = 5

while i > 0:
    print(i)
    i = i - 1


# Day 5 - Pattern Practice


# -----------------------------------
# 1. Star Triangle
# -----------------------------------
# Print increasing star pattern

rows = 5

for i in range(1, rows + 1):        # controls rows
    for j in range(i):              # controls columns
        print("*", end="")
    print()


# -----------------------------------
# 2. Number Increasing Pattern
# -----------------------------------
# Print numbers in increasing form

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# -----------------------------------
# 3. Number Decreasing Pattern
# -----------------------------------
# Print decreasing numbers

rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


# -----------------------------------
# 4. Pyramid Pattern
# -----------------------------------
# Right aligned pyramid using spaces + stars

rows = 7

for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # print stars
    for k in range(i):
        print("*", end=" ")
    
    print()



# Day 6 - Collections Practice

# List
fruits = ["apple", "banana", "mango"]
fruits.append("grapes")
fruits.insert(1, "orange")
fruits.remove("banana")
fruits.sort()
print("List:", fruits)

# Tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Set
items = {"apple", "banana", "apple", "mango"}
print("Set:", items)

# Dictionary
student = {
    "name": "Ankit",
    "age": 20,
    "course": "Python"
}
print("Dictionary:", student)

student["age"] = 21
student["gender"] = "Male"
print("Updated Dictionary:", student)



# Day 7 - Functions Practice

# Basic function
def hello():
    print("Hello Mitra")

hello()

# Function with parameter
def greet(name):
    print("Hello", name)

greet("Ankit")

# Function with return value
def add10(x):
    return x + 10

print(add10(20))

# Function with two parameters
def add(a, b):
    return a + b

print(add(45, 65))

# Even or odd checker
def evenodd(x):

    if x % 2 == 0:
        print(x, "is even")

    else:
        print(x, "is odd")

evenodd(2883)

# Factorial function
def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))

# Day 7.2 - OOP Practice

# Class and object
class Phone:
    name = "Samsung"

phone1 = Phone()
print(phone1.name)

# Attributes and methods
class Mobile:
    name = "iPhone"
    color = "Black"

    def make_call(self):
        print("Making a call")

    def play_game(self):
        print("Playing a game")

m1 = Mobile()
print(m1.name)
print(m1.color)
m1.make_call()
m1.play_game()

# Constructor
class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_details(self):
        print("The name of employee is", self.name)
        print("The age of employee is", self.age)
        print("The salary of employee is", self.salary)
        print("The gender of employee is", self.gender)

e1 = Employee("Raghu", 25, 70000, "Male")
e1.show_details()

# Student class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_result(self):
        if self.marks >= 50:
            print(self.name, "has passed")
        else:
            print(self.name, "has failed")

s1 = Student("Ankit", 20, 78)
s1.show_result()

# Car class
class Car:
    def __init__(self, brand, mileage, cost):
        self.brand = brand
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a car")
        print("Brand:", self.brand)
        print("Mileage:", self.mileage)
        print("Cost:", self.cost)

c1 = Car("BMW", 100, 2000)
c1.show_details()
