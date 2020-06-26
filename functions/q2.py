def sum_of_number_list(input_list):
  if len(input_list) == 0:
    return 0
  else:
    return input_list[0] + sum_of_number_list(input_list[1:])

print(sum_of_number_list([1,2,3,4,-5]))
print(sum_of_number_list([]))
print(sum_of_number_list([8,2,3,0,7]))