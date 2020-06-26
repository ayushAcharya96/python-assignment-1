def square_cube_list_element(input_list):
  return list(map(lambda num: (num**2, num**3), input_list))

print(square_cube_list_element([1,2,3,4,5]))