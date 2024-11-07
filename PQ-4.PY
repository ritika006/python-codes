""" Easy Level: """

 #  Q1: Write a Python function add_two_numbers(a, b) that takes two numbers as input
 #      and returns their sum.
"""
def sum(a, b):
    return a + b
"""


 #  Q2: Define a function find_maximum(a, b) that accepts two numbers and returns the
 #      larger number.
"""
def max(a, b):
    return a if a > b else b
"""


 #  Q3: Create a function is_positive(num) that checks if a given number is positive. The
 #      function should return True if the number is positive and False otherwise.
"""
def positive(num):
    return num > 0
"""


 #  Q4: Write a function print_name(name) that takes a string name and prints "My name is
 #      [name].
"""
def print_name(name):
    print(f"My name is {name}.")
"""


 #  Q5: Write a function square(x) that returns the square of a number x.
"""
def square(x):
    return x ** 2
"""




""" Medium Level: """

 #  Q6: Write a Python function find_greater_than(lst, n) that accepts a list lst of
 #      numbers and a number n. The function should return a new list containing only the
 #      numbers greater than n.
"""
def greater(lst, n):
    return [x for x in lst if x > n]
"""


 #  Q7: Create a function count_vowels(s) that takes a string s as input and returns the
 #      number of vowels in the string.
"""
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count
"""




""" Intermediate Level: """

 #  Q8: Write a Python function factorial(n) that calculates and returns the factorial of a
 #      number n using recursion.
"""
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
"""





""" Easy Level Word Problem: """

 #  Q9: Write a Python function circle_area(radius) that takes the radius of a circle and
 #      returns the area of the circle. (Use the formula: Area = π × radius², assume π = 3.1416).
"""
def circle_area(radius):
    pi = 3.1416
    return pi * (radius ** 2)
"""




""" Medium Level Word Problem: """

 #  Q10: Write a Python function monthly_payment(principal, rate, years) that
 #       calculates the monthly mortgage payment for a given principal loan amount, annual
 #       interest rate, and loan term in years. Use the formula:
"""
def monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    total_payments = years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)
    return monthly_payment
principal = 200000  
rate = 5 
years = 30
payment = monthly_payment(principal, rate, years)
print(f"Monthly mortgage payment: ${payment:.2f}")
"""
