def multiple_of_list_items(list):
  if len(list) == 0:
    return 1
  else:
    return list[0] * multiple_of_list_items(list[1:])

print(multiple_of_list_items([1, 2, 3, 4]))