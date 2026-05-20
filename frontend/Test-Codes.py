# Test comprehensive rules
import os  # Unused import

# Invalid naming
userName = "Alice"
TotalCount = 10

# Undefined variable
print(undefined_var)

# Redefined builtin
list = [1, 2, 3]

# Missing docstring
def calculate():
    unused_var = 10
    return 42

# Range len pattern
items = [1, 2, 3]
for i in range(len(items)):
    print(items[i])

# == True
flag = True
if flag == True:
    print("yes")

# Mutable default
def append_to(item, items=[]):
    items.append(item)
    return items

# No with statement
f = open('test.txt')
data = f.read()
f.close()

# Broad except
try:
    risky_operation()
except:
    pass

# Type checking
if type(items) == list:
    print("list")

# Global usage
counter = 0
def increment():
    global counter
    counter += 1





#🎯 Test Codes for DevNest
#Copy and paste these into DevNest to test different scenarios:
#________________________________________
#Test 1: Simple Code (Good) - 10 seconds
#python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#Tests: Basic structure, good practices, style suggestions
#________________________________________
#Test 2: Indentation Error - 12 seconds
#python
def my_function():
    print("Hello")
    print("World")
#Tests: Critical error detection, before/after examples
#________________________________________
#Test 3: Undefined Variable - 12 seconds
#python
x = 10
y = 20
print(result)
#Tests: Critical error (undefined variable)
#________________________________________
#Test 4: Multiple Issues - 15 seconds
#python
def calculate(x,y):
    result=x+y # indentation and spacing issues 
print(result)
#return result

calculate(5,3)
#Tests: Missing spaces, no function call result handling, style issues
________________________________________
#Test 5: Loop Optimization - 18 seconds
#python
numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print(total)
#Tests: Optimization suggestions (enumerate, sum(), +=)
________________________________________
#Test 6: No Errors (Perfect Code) - 15 seconds
#python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Python."

message = greet("Alice")
print(message)
#Tests: All green, good practices recognition
________________________________________
#Test 7: Complex Code - 25 seconds
#python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

result = fibonacci(10)
print(result)
#Tests: Complex logic analysis, performance tips
________________________________________
#Test 8: Bad Naming & Style - 14 seconds
#python
x = 5
y = 10
z = x + y
print(z)
#Tests: Variable naming suggestions, code readability
________________________________________
#Test 9: String Issues - 13 seconds
#python
name = "John"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")
#Tests: f-string suggestions
________________________________________
#Test 10: Import & Logic - 16 seconds
#python
import os
import sys

def check_age(age):
    if age > 18:
        print("adult")
    else:
        print("minor")

check_age(20)
#Tests: Unused imports, comparison operator suggestions
________________________________________
#Test 11: List Comprehension - 17 seconds
#python
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)
#Tests: List comprehension optimization
________________________________________
#Test 12: Exception Handling - 20 seconds
#python
def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(10, 0))
#Tests: Error handling suggestions, try-except
________________________________________
#Test 13: Long & Complex - 35 seconds
#python
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def calculate_average(self):
        total = 0
        for grade in self.grades:
            total = total + grade
        average = total / len(self.grades)
        return average
    
    def is_passing(self):
        avg = self.calculate_average()
        if avg >= 60:
            return True
        else:
            return False

student1 = Student("Alice", 20, [85, 90, 78, 92])
print(student1.name)
print(student1.calculate_average())
print(student1.is_passing())
#Tests: OOP analysis, optimization, multiple suggestions
________________________________________
#Test 14: Empty Code - 5 seconds
#Tests: Error handling for empty input
________________________________________
#Test 15: Syntax Error - 10 seconds
#python
print("Hello World") #remove the bracet 
print("Missing parenthesis")
#Tests: Syntax error detection;