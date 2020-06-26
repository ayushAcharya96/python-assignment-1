def insert_string_middle(string1, string2):
  middle_index = int(len(string1) / 2)
  return f'{string1[:middle_index]}{string2}{string1[middle_index:]}'

print(insert_string_middle('[[]]', 'python'))
print(insert_string_middle('[[[', 'python'))