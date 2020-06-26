def sort_list_of_tuples(input_list):
  input_list.sort(key=lambda x: x[-1])
  return input_list

print(sort_list_of_tuples([(2,5), (1,2), (4,4), (2,3), (2,1)]))
