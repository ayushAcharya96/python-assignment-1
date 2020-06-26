def create_unique_list(input_list):
  return list(dict.fromkeys(input_list))

print(create_unique_list([1,2,3,4,5,4,3,2,3,4,4,6]))