def longest_string(string_list):
  temp = ""
  for string in string_list:
    if len(temp) < len(string):
      temp = string
  return temp

print(longest_string(['ayush', 'acharya', 'apple', 'photograph', 'hippopotamus']))
print(longest_string(['a', 'ab', 'abc', 'abcd', 'abcde']))
print(longest_string([]))