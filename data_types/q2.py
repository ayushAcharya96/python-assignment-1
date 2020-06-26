
input = input('Enter a string: ')
if len(input) < 2:
  print("")
else:
  print("{}{}".format(input[:2], input[-2:]))

