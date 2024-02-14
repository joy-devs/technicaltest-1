# Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

#Fibbonacci sequence is the series of numbers where every number is found by adding two numbers before it.

a, b = 0, 1

while b < 100:
  print(b)

  a, b = b, a + b
