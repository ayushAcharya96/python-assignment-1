def replace_last_element_with_list(input_list, appending_list):
  return input_list[:-1] + appending_list

print(replace_last_element_with_list([1,2,3], ['a', 'b', 'c']))