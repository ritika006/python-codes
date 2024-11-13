"""


Easy Level: Fill in the Blanks

Define a Class
class ___class is a blueprint of a program___:
pass


1. Creating an Object
class Dog:
def __init__(self, name):
self._______name_______ = name
my_dog = Dog("Buddy")


2. Using the __init__ Method
class Car:
def __init__(self, make, model):
self.make = ______make________
self.model = _______model_______
my_car = Car("Toyota", "Corolla")


3. Accessing Attributes
class Person:
def __init__(self, name):
self.name = name
p = Person("Alice")
print(p._____Person_________) # Should print Alice


4. Defining a Method
class Calculator:
def add(self, a, b):
return a + __b__
calc = Calculator()
print(calc.add(2, __3__)) # Should print 5 if the second
argument is 3


5. Class Attributes
class Circle:
pi = 3.14 # ____pi____ is a class attribute
print(Circle._pi_) # Should print 3.14


6. Instance Attributes
class Book:
def __init__(self, title):
self.title = ____title____
my_book = Book("1984")
print(my_book._____Book_____) # Should print 1984




7.
Mid-Level Coding Problems

1. Create a Class with Methods
○ Define a class Rectangle that has methods to calculate the area and
perimeter. Instantiate the class and print the results.
class Rectangle:
def __init__(self, width, height):
self.width = width
self.height = height
def area(self):
return ______________
def perimeter(self):
return ______________
rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


2. Inheritance
○ Create a base class Animal and a subclass Dog. The subclass should have
a method that overrides a method from the base class.
class Animal:
def speak(self):
return "Animal sound"
class Dog(Animal):
def ______________:
return "Bark"
my_dog = Dog()
print(my_dog.speak()) # Should print "Bark"


3. Polymorphism
○ Create two classes Cat and Dog, both having a method speak.
Demonstrate polymorphism by calling the method on both objects.
class Cat:
def speak(self):
return "Meow"
class Dog:
def ______________:
return "Woof"
def animal_sound(animal):
print(animal.speak())
my_cat = Cat()
my_dog = Dog()
animal_sound(my_cat) # Should print "Meow"
animal_sound(my_dog) # Should print "Woof"


5 Static Methods
● Create a class MathUtils with a static method add that takes two
numbers and returns their sum.
class MathUtils:
@staticmethod
def ______________(a, b):
return a + b
print(MathUtils.add(5, 10)) # Should print 1

"""