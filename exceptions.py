"""
Exceptions are errors detected during execution. They disrupt the normal flow
of a program

Why use it?
Prevent program crashing
Allows graceful recovery
Helps debugging and maintaining code

try:
    code that may throw an error
except Exception Type:
    code that handles the exception
"""

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero, and neither can I...")
except ValueError:
    print("Invalid input, give me a number > 0")


try:
    result = 10 / 0
# catch all - use sparingly...
except Exception as e:
    print(type(e))
    print(f"An exception occured: {e}")

"""
Using else with try and except...
The else block executes if no exceptions occur
try:
    code
except Exception:
    handle exception
else:
    executes if no exeception
"""
try:
    x = int(input("Enter a number: "))
    result = 1000 / x
except ZeroDivisionError:
    print("You cannot divide by zero, and neither can I...")
except ValueError:
    print("Invalid input, give me a number > 0")
else:
    print(f"Answer is {result}")

"""
The finally block 
executes code regardless of whether an exception occured
useful for cleanup like closing a file
try:
    code
except Exception:
    handling
finally:
    always run - cleanup
"""

try:
    file = open("cards.py", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleaning up resources, closed file reader")


def check_positive(number):
    if number <= 0:
        raise ValueError("Number has to be positive and above zero")
    return number


try:
    print(check_positive(-5))
except ValueError as v:
    print(v)


"""
Define your own exceptions by inheritance... from the Exception class
"""


class CustomError(Exception):
    pass


try:
    raise CustomError("This is that special custom error!")
except CustomError as odd_message:
    print(odd_message)


class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("You must be 18 to but our alcoholic drinks")


try:
    answer = int(input("What is your age?: "))
    check_age(answer)
except ValueError:
    print("You must enter a number")
except AgeError as e:
    print(e)
else:
    print("Thanks your order is on it's way")
finally:
    print("Do drop by again")

