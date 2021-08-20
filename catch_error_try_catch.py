#try except block to handle error
try:
  answer = 10/0
  number = int(input("Enter a number: "))
  print(number) 
except ZeroDivisionError as err:
  print(err)
except ValueError:
  print("invalid input")

