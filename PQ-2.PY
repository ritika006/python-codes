# Question 1: Write a Python program to check if a string is a palindrome (reads the sameforwards and backwards).
"""
def palidrome(s):
    return s == s[::-1]
string = input("Enter a string: ")
if palidrome(string.lower()):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""


# Question 2: Write a Python program to count the number of vowels in a given string.
"""
def count_v(s):
    vowels = "aeiouAEIOU"
    Count = 0
    for char in s:
        if char is vowels:
            Count += 1
    return Count
string = input("Enter a string: ")
count_v = count_v(string)
print(f"The no. of  vowels in the string is {count_v}")
"""


# Question 3: Write a Python program to find the length of a given string without using the built-in len() function.
"""
def length(s):
    count = 0
    for i in s:
        count += 1
    return count
string = input("Enter a string: ")
print(f"The length of the string is {length(string)}")
"""


# Question 4: Write a Python program to convert a string to uppercase and lowercase.
"""
def case(s):
    uppercase = s.upper()
    lowercase = s.lower()
    return uppercase, lowercase
string = input("Enter a string: ")
upper, lower = case(string)
print(f"The uppercase of the string is {upper}")
print(f"The lowercase of the string is {lower}")
"""


# Question 5: Write a Python program to find the first occurrence of a substring in a given string.
"""
def occurrence(first_string, second_string):
    position = first_string.find(second_string)
    if position != -1:
        print(f"The first occurrence of '{second_string}' is at index {position}.")
    else:
        print(f"'{second_string}' not found in the given string.")     
first_string = input("Enter the main string: ")
second_string = input("Enter the substring to find: ")
occurrence(first_string, second_string)
"""


# Question 6: Write a Python program to replace all occurrences of a word in a string with another word.
"""
def replace(original_string, old_word, new_word):
    updated_string = original_string.replace(old_word, new_word)
    return updated_string
original_string = input("Enter the original string: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")

result = replace(original_string, old_word, new_word)
print("Updated string:", result)
"""


# Question 7: Write a Python program to reverse a string.
"""
string = "Shakalaka Bum Bum!"
print(string[::-1])
"""


# Question 8: Write a Python program to check if two strings are anagrams (contain the same characters in a different order).
"""
def anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
"""


# Question 9: Write a Python program that takes a sentence as input and counts the number of
#             words in it. A word is defined as a sequence of characters separated by spaces.
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")
"""


# Question 10: Write a Python program that takes a string as input and returns a new string
#              where each word's first letter is capitalized (also known as "title case"). For example, the input
#             "hello world" should return "Hello World". Consider edge cases like multiple spaces
#              between words.
"""
def case(sentence):
    words = sentence.split() 
    title_cased_sentence = ' '.join([word.capitalize() for word in words])
    return title_cased_sentence
sentence = input("Enter a sentence: ")
title_cased_sentence = case(sentence)
print("Title cased sentence:", title_cased_sentence)
"""