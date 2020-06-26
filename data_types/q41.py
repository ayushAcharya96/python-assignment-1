def convert_into_string(input_tuple):
  result = ''
  for item in input_tuple:
    result += str(item)
  return result

print(convert_into_string((1,2,3,4)))