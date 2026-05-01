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
