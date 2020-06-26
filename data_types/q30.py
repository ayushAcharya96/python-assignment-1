def key_exists_in_dict(input_dict, key):
  if key in input_dict.keys():
    return True
  return False

print(key_exists_in_dict({1:10, 2:20, 3:30}, 5))