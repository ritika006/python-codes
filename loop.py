#Write a program to print your name 10 times using for loop.
"""
for i in range(10):
    print("Ritika")
"""


#write a program to take name from user and print it 10 times.
"""
a = input("Enter your name")
for i in range(10):
    print(a)
"""


#Write a program to count total number of digits in a number.
"""
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Total number of digits: ", count)
"""


#write a program to accept a no. from 1 to 12 and display name of the month like 1 for january and number of days 31 and so on.
"""
month_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = int(input("Enter a number from 1 to 12: "))

while num < 1 or num > 12:
    print("Invalid input. Please enter a number from 1 to 12.")
    num = int(input("Enter a number from 1 to 12: "))

print("Month:", month_names[num])
print("Number of days:", month_days[num])
"""


# Write the logical expression for the following: A is greater than B and C is greater than D
"""
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))
C = int(input("Enter value of C: "))
D = int(input("Enter value of D: "))

expression = (A > B) and (C > D)

print("The logical expression is:", expression)
"""


# WAP to print first  10 natural numbers using while loop.
"""
i = 1
while i <= 10:
    print(i)
    i += 1
"""


# WAP to calculate sum of all even no. starting from 1 to 100.
"""
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("Sum of even numbers from 1 to 100:", sum_even)
"""


# WAP to print table of 22, 55, 66, 19, 15.
"""
for num in [22, 55, 66, 19, 15]:
    print("Table of", num, ":")
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print()
"""





