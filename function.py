# User defined function
"""
def square(num):
    This function computes the square of the no.
    return num ** 2
object_=square(6)
print("The square of the given no. is",object_)
"""


# WAP to check whether a person is eligible for voting or not.(voting age >>18)
"""
def check_age(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
age = int(input("Enter your age: "))
print(check_age(age))
"""


#QUESTIONS
# WAP to find to check whether a no. is entered by user is divisible by 2 and 3 both. (entered no. should not be greater than 100)
"""
num = int(input("Enter a number (less than or equal to 100): "))
if num <= 100:
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3.")
    else:
        print(f"{num} is not divisible by both 2 and 3.")
else:
    print("Please enter a number less than or equal to 100.")
"""


# WAP to find largest of 3 no. inputed by user.
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)
"""

            
# WAP to check a character is vowel or not.
"""
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels
char = input("Enter a character: ")
if is_vowel(char):
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
"""

    

# Write a program to check whether a no. is prime or not.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n **  0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""
# OR
"""
    k=0
    num1 = int(input("Enter any no."))
    if num1 == 0 or num1 == 1:
        k=1
        for i in range(2,num1):
            if (num1%i == 0):
                k=1
            if k==1:
                print("no. is not prime")
        else:
            print("no. is prime")
"""