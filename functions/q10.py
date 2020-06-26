def find_even_from_list(input_list):
  for element in input_list:
    if element % 2 == 0:
      print(element)

find_even_from_list([2,3,4,23,5,42,54,66,34,33,9])