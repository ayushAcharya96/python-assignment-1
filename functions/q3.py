def product_of_number_list(input_list):
  if len(input_list) == 0:
    return 1
  else:
    return input_list[0] * product_of_number_list(input_list[1:])

print(product_of_number_list([8,2,3,-1,7]))