# Question 1- Print numbers from 1 to 10 using a for loop
"""
    for i in range(1,11):
    print(i) 
"""


# Question 2- Calculate the sum of numbers from 1 to 10 using a for loop
"""
sum  = 0
for n in range(1,11):
    sum += n
    print(sum)
"""


# Question 3- Print even numbers from 1 to 10 using a for loop
"""
e =  0
for i in range(2,11,2):
    e += i
    print("Sum of even no. from 1 to 10 is",e)
"""


# Question 4- Print numbers in reverse from 10 to 1 using a for loop
"""
start = 10
end = 1
for i in range(start, end -1,-1):
    print(i)
"""


# Question 6- Print characters of a string using a for loop
"""
my_string = "Hello Ritika!"
for i in my_string:
    print(i)
"""


# Question 7- Find the largest number in a list using a for loop
"""
num = [12, 45, 66, 74, 9, 11, 6]
largest_num = num[0]
for i in num:
    if i > largest_num:
        largest_num = i
        print("Largest number in the list is:", largest_num)
"""


# Question 8- Find the average of numbers in a list using a for loop
"""
numbers = [12, 45, 7, 23, 56, 89, 34]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
average = sum_of_numbers / len(numbers)
print("The average of the numbers in the list is:", average)
"""

# Question 9- Count the number of vowels in a string using a for loop
"""
my_string = "Hello, Ritika!"
vowel_count = 0
vowels = 'aeiouAEIOU'
for char in my_string:
    if char in vowels:
        vowel_count += 1
print("The number of vowels in the string is:", vowel_count)
"""


# Question 10- Print a pattern of stars using nested for loops
"""
rows = 10
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
"""


# Question 11- Calculate factorial of a number using a while loop
"""
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
"""


# Question 12- Find the first occurrence of a number in a list using a while loop
"""
def find_first_occurrence(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            return index
        index += 1
    return -1
my_list = [1, 2, 3, 1, 6, 2, 3, 9, 2]
target_num = 2
result = find_first_occurrence(my_list, target_num)
if result !=  -1:
    print(f"The first occurrence of {target_num} is at index {result}")
else:
    print(f"{target_num} is not found in the list")
"""


# Question 13- Calculate the sum of numbers from 1 to 100 usinga while loop
"""
def sum():
    total_sum = 0
    number = 1
    while number <= 100:
        total_sum += number
        number += 1
    return total_sum
result = sum()
print(f"The sum of numbers from 1 to 100 is: {result}")
"""


# Question 14- Find all prime numbers between 1 and 50 using nested for and if
"""
def find_primes():
    primes = []
    for num in range(2, 51):
        is_prime = True 
        for i in range(2, num):
            if num % i == 0:
                is_prime = False  
                break
        if is_prime:
            primes.append(num)
    return primes
prime_numbers = find_primes()
print("Prime numbers between 1 and 50 are:", prime_numbers)
"""


# Question 15- Print the Fibonacci sequence up to the 10th term
"""
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci_sequence(10)
"""


# Question 16- Print numbers in a list until a negative number isencountered using a while loop
"""
def print_until_negative(numbers):
    index = 0
    while index < len(numbers) and numbers[index] >= 0:
        print(numbers[index])
        index += 1
numbers = [3, 7, 12, 5, -1, 9, 8]
print_until_negative(numbers)
"""


# Question 17- Print numbers from 1 to 10. If a number is divisibleby 4, stop the loop using a for loop and break statement
"""
def print_numbers():
    for num in range(1, 11):
        if num % 4 == 0:
            break
        print(num)
print_numbers()
"""

# Question 18- Print numbers from 1 to 10. If a number is even,skip it using a for loop and else clause
"""
for num in range(1, 11):
    if num % 2 != 0:
        print(num)
"""


# Question 19- Python program to check if a given number is an Armstrong number
"""
def is_armstrong_number(num):
    str_num = str(num)
    num_digits = len(str_num)
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    return armstrong_sum == num
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
"""


# Question 20- Python program to convert the month name to a number of days
"""
def month_to_days(month_name):
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return month_days.get(month_name.title(), "Invalid month name")
month_name = input("Enter the month name: ")
num_days = month_to_days(month_name)
print(f"{month_name} has {num_days} days")
"""