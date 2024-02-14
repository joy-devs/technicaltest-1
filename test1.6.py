# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.

# eg " Hello World " => returns 2

sentence = "web development"

count = len([char for char in sentence if char in "aeiou"] )

print("number of vowels  in the string is :", count)