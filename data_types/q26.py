def append_string_to_list_elements(input_list, append_string):
  return [append_string + str(element) for element in input_list]


print(append_string_to_list_elements([1,2,3,4], 'emp'))