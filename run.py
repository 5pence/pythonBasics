from math import sqrt, pi, sin

print("Hello World")

# Variables and Data Types
x = 5             # int
name = "Alice"    # str
PI = 3.14159      # float
is_active = True  # bool

# type conversion
num_str = "42"
num = int(num_str)
print(num + 10)

a = 10
b = 3

print(a + b) # 13
print(a * b) # 30
print(a - b) # 7
print(a / b) # 3.333333333...
print(a // b) # 3 integer division
print(a % b) # 1 modulo (gives remainer)
print(a ** b) # 1000 exponent

# String Operations
s = "Hello"
print(s + " World") # Hello World
print(s * 3) # HelloHelloHello
print(s[1])  # e
print(s[1:4])  # ell
print(s[:2])  # He
print(s[2:])  # llo
print(s[-1])  # o

# Conditional Statements
x = 7
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is 10")
else:
    print("x is less than 10")

# Loops
for i in range(100):
    print(i)    # will print 0 to 99

print("=====================")
print("""
    This is a multiline print
    statement
      """)
print("=====================")
for i in range(13):
    print(f"{i} * 7 = {i*7}")

a = 987
print(12**a)

fruits = ["apple", "banana", "cherry", "dragon fruit"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print("Count is ", count)
    count += 1


# this function says bye
def bye():
    return "bye"


def greet(name="harry"):
    """
    This greet method take a string name and returns a greeting
    if no name is given a default arguement of 'harry' is used
    """
    return "Hello, " + name


s = greet("Sonali")
print(s)
print(greet())

# Data Structures
# Lists - ordered and mutable
my_list = [1, 2, 3, "four"]
my_list.append(5)
print(my_list)

# Tuples - ordered and immutable sequences
my_tuple = (1, 2, 3)
# my_tuple[0] = 10 # its immutable, thats why!

# Dictionaries
person = {
    "name": "Alice",
    "age": 25
}
print(person["name"])
person["age"] = 26
print(person["age"])

# Sets: Unordered collections of unique elements
my_set = {1, 2, 3, 2, 2, 5, 3, 7, 1, 1, 2, 2}
print(my_set)

# input and output

name = input("Enter your name: ")
print(f"Hello {name}")

# Basic error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("You cannot divide by zero again!")

print(sqrt(16)) # 4.0
print(pi)
print(sin(pi/2))
