def reverse_string(input_string):
  result_string = ''
  for char in input_string:
    result_string = char + result_string
  return result_string

print(reverse_string('python'))
print(reverse_string('abcdefghij'))