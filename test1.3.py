# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

def is_power_of_two(num) :
  return num > 0 and (num & (num-1)) ==0
user_input= int(input("Enter num:"))
    
answer = is_power_of_two(user_input)

  
print(answer)