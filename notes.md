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
