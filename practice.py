###Day
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

