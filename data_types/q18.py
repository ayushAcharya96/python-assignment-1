def largest_number_in_list(list):
  list.sort()
  return list.pop()

print(largest_number_in_list([1,2,2,1,2,6,3,1,2]))