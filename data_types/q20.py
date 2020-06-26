def number_of_string(list):
  result = 0
  for string in list:
    if len(string) >= 2 and string[0] == string[-1]:
      result += 1
  return result

print(number_of_string(['abc', 'xyz', 'aba', '1221']))
