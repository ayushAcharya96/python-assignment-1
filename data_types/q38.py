def remove_key_from_dict(input_dict, key):
  input_dict.pop(key, None)
  return input_dict

print(remove_key_from_dict({1:10, 2:20}, 1))
print(remove_key_from_dict({1:10, 2:20}, 5))