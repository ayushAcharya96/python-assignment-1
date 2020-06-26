def clone_list(input_list):
  return input_list.copy()

vowels = ['a', 'e', 'i', 'o', 'u']
test = vowels
clone = clone_list(vowels)

print(hex(id(vowels)))
print(hex(id(test)))
print(hex(id(clone)))