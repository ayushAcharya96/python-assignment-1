def remove_nth_index(string, index):
  return f'{string[:index]}{string[index+1:]}'

print(remove_nth_index('ayush', 3))
print(remove_nth_index('ayush', 0))
print(remove_nth_index('ayush', 4))