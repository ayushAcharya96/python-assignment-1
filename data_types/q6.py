input = input('Enter string: ')
index_of_not = input.find('not')
if index_of_not > -1:
  index_of_poor = input.find('poor', index_of_not)
  if index_of_poor > -1:
    print(f'{input[:index_of_not]} good{input[index_of_poor + 4:]}')
  else:
    print(input)
else:
  print(input)