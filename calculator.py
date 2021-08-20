# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + float(num2)
# print(result)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: 7"))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "*":
  print(num1 * num2)
elif operator == "/":
  print(num1 / num2)
else: 
  print("Invalid operator")

