input = input('Enter a string: ')
if len(input) >= 3:
  if input[-3:] == 'ing':
    print(input + 'ly')
  else:
    print(input + 'ing')
