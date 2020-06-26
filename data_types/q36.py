def sum_of_dict_items(input_dict):
  result = 0
  for value in input_dict.values():
    result += value
  return result

print(sum_of_dict_items({1:10, 2:20, 3:30}))