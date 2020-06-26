input = input('Enter a string: ')
result = ""
first_char = input[0]
for char in input:
  if result != "" and char == first_char:
    result += '$'
  else:
    result += char
print(result)