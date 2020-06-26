def remove_item_from_tuple(input_tuple, item):
  index = input_tuple.index(item)
  return input_tuple[:index] + input_tuple[index + 1:]

print(remove_item_from_tuple((1,2,3), 2))