def calculate_factorial(number):
  if number == 0:
    return 1
  else:
    return number * calculate_factorial(number - 1)

print(calculate_factorial(5))
print(calculate_factorial(0))