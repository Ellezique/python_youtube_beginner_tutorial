is_male = True
is_tall = True

if is_tall and is_male:
  print("You are male and tall")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are tall. You are not male.")
else:
  print("You are either not tall or not male or neither")

#use comparisons in if statements
#comparison operators: ==  !=  
def max_num(num1, num2, num3):
  if num1>= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >=num3:
    return num2
  else:
    return num3

print(max_num(3, 4, 5))