def is_dict_list_empty(input_list):
  for dicts in input_list:
    if dicts:
      return False
  return True

print(is_dict_list_empty([{}, {}, {}]))
print(is_dict_list_empty([{1,2}, {}, {}]))