# Python Notes 

---

## 1. Variables
Variables are used to store data in memory.

Example:
x = 10
name = "Ankit"

---

## 2. Data Types

### int
Whole numbers  
Example: 10, 50  

### float
Decimal numbers  
Example: 9.5, 3.14  

### str
Text data  
Example: "Hello"  

### bool
True or False values  
Example: True, False  

---

## Example of Data Types

name = "Ankit"   # string  
age = 20         # int  
price = 99.5     # float  
x = True         # bool  

---

## 3. Type Checking

type(name)   → str  
type(age)    → int  
type(price)  → float  

---

## 4. Operators

### Arithmetic Operators
  +  → addition  
  -  → subtraction  
  *  → multiplication  
  /  → division  
   
Example:
a = 2  
b = 5  

a + b = 7  
a * b = 10  

---

### Relational Operators
== → equal  
!= → not equal  
>  → greater than  
<  → less than  

Example:
a = 2  
b = 5  

a < b → True  
a > b → False  

---

### Logical Operators
and → both conditions must be True  
or  → at least one True  
not → reverse result  

Example:
True and True → True  
True or False → True  
not True → False  

---

## 5. Common Mistake (Important )

name = "apple"  
number = 10  

print(name + number) ERROR  

### Reason:
Cannot add string and integer directly  

### Fix:
print(name + str(number)) ✔  

Output:
apple10  

---

## Summary
- Variables store data  
- Data types define type of data  
- Operators perform operations  
- Type conversion is important 
-
-
- 

## Day one common Mistakes & Fix 

###  Mistake 1: Adding string and integer

name = "apple"
number = 10

print(name + number)

 Error: TypeError

###  Reason:
Python cannot add different data types directly (string + integer)

###  Fix:

print(name + str(number))

 Output:
apple10

---

###  Mistake 2: Wrong type assumption

x = "10"
y = 5

print(x + y)

 Error: TypeError

###  Reason:
"x" is a string, not a number

###  Fix:

print(int(x) + y)

 Output:
15

---

### Mistake 3: Division confusion

a = 5
b = 2

print(a / b)

Output: 2.5 (float)

###  Reason:
Normal division always returns float

###  Fix (if integer needed):

print(a // b)

 Output:
2

---

###  Mistake 4: Boolean confusion

print(True + True)

 Output: 2

###  Reason:
True = 1 and False = 0 in Python

###  Understanding:
True + True = 1 + 1 = 2

---

##  Summary
- Always check data types  
- Use type conversion when needed  
- Read error messages carefully


#### Day 2 - Strings, Input, Indexing, Slicing

---

## String
A string is text inside quotes.

Example:
name = "Ankit"

---

## print()
Used to display output.

Example:
print("Hello")

---

## input()
Used to take input from user.
It returns data as string.

Example:
name = input("Enter your name: ")

---

## Indexing
Indexing means accessing one character from a string.

Example:
word = "PYTHON"

word[0] → P  
word[-1] → N  

---

## Slicing
Used to get part of a string.

Example:
text = "Hello"

text[0:4] → Hell  
text[:3] → Hel  
text[3:] → lo  

---

## String Methods
upper() → capital letters  
lower() → small letters  
strip() → remove spaces  
replace() → change text  

Example:
msg = " hello "
msg.strip().upper()

---

## Type Conversion
input() gives string by default.

To use numbers:
int() → convert to number  
str() → convert to string  

Example:
age = int(input("Enter age: "))
print(age + 5)

---

## Common Mistake 

num1 = input("First: ")
num2 = input("Second: ")

print(num1 + num2) ❌ (joins text)

Fix:
print(int(num1) + int(num2)) 



# Day 3 - If Else

## Concepts

### If Else
Used to make decisions based on conditions.

Example:
if age >= 18:
    print("Adult")
else:
    print("Minor")

---

### Elif
Used when there are multiple conditions.

Example:
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

---

## Key Points
- Conditions must be True or False
- Indentation is important
- Only one block runs in if-elif-else



# Day 4 - Loops

---

## What is a Loop?
A loop is used to repeat a block of code multiple times.

---

## Types of Loops

### 1. for loop
Used when we know how many times we want to repeat something.

Example:
for i in range(5):
    print(i)

---

### 2. while loop
Used when we want to repeat code based on a condition.

Example:
count = 0

while count < 5:
    print(count)
    count += 1

---

## range()

range() is used to generate a sequence of numbers.

- range(5) → 0 to 4  
- range(1, 5) → 1 to 4  

The last value is not included.

---

## Key Points

- Loops are used for repetition  
- for loop → fixed number of times  
- while loop → condition-based  
- range() helps generate numbers  
- Indentation is very important  

---

## Common Mistake

Wrong:
while count < 5:
print(count)

Correct:
while count < 5:
    print(count)

Without indentation, Python will give an error.



# Day 5 - Patterns

---

## What is a Pattern?

A pattern is printing shapes (stars, numbers, etc.) using loops.

---

## Key Idea

- Outer loop → controls rows  
- Inner loop → controls columns  

If the inner loop does not depend on the outer loop,
the same pattern will repeat on every row.

---

## Types of Patterns

### 1. Star Pattern
*
**
***
****
*****

### 2. Number Pattern
1
12
123
1234

### 3. Reverse Pattern
54321
4321
321
21
1

### 4. Pyramid Pattern
    *
   * *
  * * *
 * * * *
* * * * *

---

## Important Concepts

- Nested loops are required  
- range() controls how many times loop runs  
- end="" keeps output on same line  
- print() moves to next line  

---

## Common Mistakes

1. Inner loop not depending on outer loop  
→ same line repeats  

2. Wrong range values  
→ pattern shape becomes incorrect  

3. Forgetting end=""  
→ output goes to next line  

4. Confusion between rows and columns  

---

## Summary

- Patterns are built using nested loops  
- Outer loop controls rows  
- Inner loop controls columns  
- Logic is more important than memorizing






# Day 6 - Collections

## List
A list is ordered and changeable.

Example:
fruits = ["apple", "banana", "mango"]

## Tuple
A tuple is ordered and not changeable.

Example:
colors = ("red", "green", "blue")

## Set
A set is unordered and stores unique values only.

Example:
items = {"apple", "banana", "apple"}

## Dictionary
A dictionary stores key-value pairs.

Example:
student = {
    "name": "Ankit",
    "age": 20
}

## Important Points
- List is changeable
- Tuple is not changeable
- Set removes duplicates
- Dictionary uses keys to access values

# Day 7 - Functions

## What is a Function?
A function is a reusable block of code that performs a specific task.

## Why Functions Are Useful
- avoid repeated code
- make programs cleaner
- improve readability
- organize logic properly

## Function Syntax
def hello():
    print("Hello")

## Parameters
Parameters are values passed into a function.

Example:
def greet(name):
    print("Hello", name)

## Return Value
return sends a value back from a function.

Example:
def add(a, b):
    return a + b

## Default Argument
A default argument gives a value if nothing is passed.

Example:
def welcome(name="Guest"):
    print("Welcome", name)

## Important Points
- use def to define functions
- use parameters to pass data
- use return when output is needed later
- functions help reuse logic


# Day 7.2 - OOP Basics

## What is OOP?
Object Oriented Programming is a way of writing code using classes and objects.

## Class
A class is a blueprint for creating objects.

## Object
An object is created from a class.

## Attributes
Attributes store data inside an object.

## Methods
Methods are functions inside a class.

## Constructor
A constructor is a special method that runs automatically when an object is created.

## self
self refers to the current object.

## Important Points
- use class to create a class
- use __init__ for constructor
- use self inside methods
- create objects to use class features


 
 
 # Day 8 - File Handling, Exception Handling and Modules

## File Handling
File handling is used to read, write and update files.

Modes:
- r → read
- w → write
- a → append

Functions:
- open()
- read()
- write()
- close()

## Exception Handling
Exception handling prevents program crashes.

Keywords:
- try
- except
- finally

## Modules
Modules help reuse code.

Examples:
- math
- random

## Import
import is used to use modules in Python.
