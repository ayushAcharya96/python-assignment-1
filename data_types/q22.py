def remove_duplicate_from_list(input_list):
  input_list = list(dict.fromkeys(input_list))
  return input_list

print(remove_duplicate_from_list([1,3,4,2,5,2,3,6,7,2,3,4]))