def remove_odd_index_character(string):
  result = ""
  for i in range(0, len(string)):
    if i % 2 == 0:
      result += string[i]
  return result

print(remove_odd_index_character('python language is the best.'))