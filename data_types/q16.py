def sum_of_elements_in_a_list(list):
  if len(list) == 0:
    return 0
  else:
    return list[0] + sum_of_elements_in_a_list(list[1:])

print(sum_of_elements_in_a_list([1, 2, 3, 4, 5, 6]))