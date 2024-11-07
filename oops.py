# CLASSES:
"""
class Apple():
    colour=""
    flavour=""

jonagold=Apple()
jonagold.colour="red"
jonagold.flavour="sweet"

print(jonagold.flavour)
"""



# print(dir(""))
# print(help("str"))



# METHODS:
"""
class elephant():
    name="Elli"
    def speak(self):
        print("eee!.I am {} eee".format(self.name))
       
hemlet=elephant()
hemlet.name="eeva"
hemlet.speak()

animal=elephant()
animal.name="voli"
animal.speak()
"""


# CONSTRUCTOR:
"""
class Apple():
    def __init__(self,colour,flavour):
        self.flavour=flavour
        self.colour=colour
jonagold=Apple("red","sweet")
print(jonagold.flavour)
"""


# INHERITANCE:
"""
class Fruit():
    def __init__(self,color,flavour):
        self.color=color 
        self.flavour=flavour 
class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
gramy= Apple("green","tart")
print(gramy.flavour)
"""


"""
class Animal():
    sound=""
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("{sound} i'm {name}, ! {sound}".format(name=self.name, sound=self.sound))

class piglet(Animal):
    sound="oink"
hamlet=piglet("Pig")
hamlet.speak()
"""


#Question- write a python fuction to find maximum of 3 no.s
"""
def max(num1, num2, num3):
    return max(num1, num2, num3)
result = max(10, 20, 15)
print(result)  
"""


#Question- write a python function to sum all the no.s in a list.
"""
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(result)  
"""


#Question- write a python function  to multiply all the no.s in a list.
"""
def mul_list(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
numbers = [6, 3, 9, 11, 2]
result = mul_list(numbers)
print(result)
"""


#Question- Write a python program to reverse a string.
"""
name = "RITIKA SHAH"
print(name[::-1])
"""


#Q- Write a python function to calculate the factorial of a no.(a non-negative no.). The function accepts the no. as an argument
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