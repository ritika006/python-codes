""" LISTS """

#1.   Basic List Creation: Create a list of 5 integers and print the sum of all the elements.
"""
integers_list = [12, 7, 23, 9, 31]
sum_of_elements = sum(integers_list)
print("The sum of the elements is:", sum_of_elements)
"""


#2.   Indexing: Given the list numbers = [3, 8, 2, 10, 6], print the first, last, and
#       middle elements of the list.
"""
numbers = [3, 8, 2, 10, 6]
first_element = numbers[0]
last_element = numbers[-1]
middle_element = numbers[len(numbers) // 2]
print("First element:", first_element)
print("Middle element:", middle_element)
print("Last element:", last_element)
"""


#3.   Slicing: For the list fruits = ['apple', 'banana', 'cherry', 'date',
#       'elderberry'], slice the list to print the first three elements.
"""
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)
"""


#  4. List Methods: Given the list colors = ['red', 'green', 'blue'], add 'yellow'
#       at the end of the list and then remove 'green'.
"""
colors = ['red', 'green', 'blue']
colors.append('yellow')
colors.remove('green')
print("Modified list of colors:", colors)
"""


#  5. List Comprehension: Generate a list of squares of numbers from 1 to 10 using list
#       comprehension.
"""
squares = [x**2 for x in range(1, 11)]
print(squares)
"""


#  6. Nested List: Create a 2D list representing a 3x3 matrix and access the element in the
#       second row and third column.
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
element = matrix[1][2]
print(f"Element in the second row and third column: {element}")
"""





""" TUPLE """

#1.   Basic Tuple Creation: Create a tuple of 4 strings and print its second element.
"""
my_tuple = ("apple", "banana", "cherry", "date")
print(f"The second element is: {my_tuple[1]}")
"""


#2.   Immutability: Why can’t we modify the elements of a tuple? Demonstrate an example of
#       an error that occurs when trying to modify a tuple.
"""
my_tuple = (10, 20, 30, 40)
try:
    my_tuple[1] = 25
except TypeError as e:
    print(f"Error: {e}")
"""


#3.   Tuple Unpacking: Given the tuple coords = (3, 5, 7), unpack the tuple into three
#       variables and print each one.
"""
coords = (3, 5, 7)
x, y, z = coords
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
"""


#4.   Tuple Concatenation: Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print
#       the result.
"""
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)
"""


#5.   Conversion: Convert the list [10, 20, 30] into a tuple and print the resulting tuple.
"""
my_list = [10, 20, 30]
resulting_tuple = tuple(my_list)
print(resulting_tuple)
"""


#6.   Finding Elements: Given the tuple letters = ('a', 'b', 'c', 'd'), check if
#       the element 'e' is present in the tuple and print a message accordingly.
"""
letters = ('a', 'b', 'c', 'd')
if 'e' in letters:
    print("'e' is present in the tuple.")
else:
    print("'e' is not present in the tuple.")
"""





""" DICTIONARY """

#1.   Basic Dictionary Creation: Create a dictionary where the keys are fruits and the values
#       are their prices. Print the price of an 'apple'.
"""
fruit_prices = {
    'apple': 1.2,
    'banana': 0.5,
    'orange': 0.8,
    'grape': 2.0
}
print("The price of an apple is:", fruit_prices['apple'])
"""


#2.   Adding and Modifying Entries: Add a new entry 'orange': 30 to the dictionary
#       {'apple': 50, 'banana': 20} and modify the price of 'banana' to 25.
"""
fruit_prices = {'apple': 50, 'banana': 20}
fruit_prices['orange'] = 30
fruit_prices['banana'] = 25
print(fruit_prices)
"""


#3.   Accessing Keys and Values: Given the dictionary student = {'name': 'John',
#       'age': 22, 'course': 'Computer Science'}, print all the keys and values.
"""
student = {'name': 'John', 'age': 22, 'course': 'Computer Science'}
for key, value in student.items():
    print(f"{key}: {value}")
"""


#4.   Dictionary Methods: Use the .get() method to safely access the price of 'grape' from
#       the dictionary {'apple': 50, 'banana': 20, 'orange': 30}.
"""
fruit_prices = {'apple': 50, 'banana': 20, 'orange': 30}
grape_price = fruit_prices.get('grape', 'Price not found')
print("The price of 'grape' is:", grape_price)
"""


#5.   Dictionary Iteration: Write a loop to iterate over the dictionary {'A': 90, 'B': 80,
#       'C': 70} and print each key-value pair.
"""
grades = {'A': 90, 'B': 80, 'C': 70}
for key, value in grades.items():
    print(f"{key}: {value}")
"""


#6.   Dictionary Comprehension: Create a dictionary where the keys are numbers from 1 to
#       5 and the values are their squares using dictionary comprehension.
"""
squares = {x: x**2 for x in range(1, 6)}
print(squares)
"""





# WORD PROBLEMS --

""" 1. Easy Level (Shopping List): You have a list of items you want to buy from the market:
        ['apple', 'banana', 'milk', 'bread', 'eggs']. Write a program that adds
        'chocolate' to the end of your shopping list and removes 'milk'. Finally, print the updated
        shopping list. """

#       shopping_list = ['apple', 'banana', 'milk', 'bread', 'eggs']
#       shopping_list.append('chocolate')
#       shopping_list.remove('milk')
#       print(shopping_list)





""" 2. Mid Level (Student Grades): You are given a list of tuples where each tuple contains a
        student's name and their score on a test:
        students = [('Alice', 85), ('Bob', 90), ('Charlie', 78),
        ('David', 92)].
        Write a program that converts this list into a dictionary where the student's name is the
        key and their score is the value. Then, print the names of students who scored above 80. """

#       students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]
#       student_grades = {name: score for name, score in students}
#       print("Students who scored above 80:")
#       for name, score in student_grades.items():
#           if score > 80:
#               print(name)
