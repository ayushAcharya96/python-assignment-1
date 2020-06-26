def multiple_of_dict_items(input_dict):
  result = 1
  for value in input_dict.values():
    result *= value
  return result

print(multiple_of_dict_items({1:10, 2:20, 3:30}))