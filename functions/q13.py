def sort_list_using_lambda(input_list):
  input_list.sort(key= lambda x:x[0])
  return input_list

print(sort_list_using_lambda([(1667, 'Ayush Acharya', 'ayush@abc.com')
 ,(213, 'john doe','john@abc.com'), (2325, 'harry potter', 'harry@abc.com')]))