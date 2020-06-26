def count_word_frequency(string):
  string = string.lower()
  word_list = string.split()
  word_dict = {}
  for word in word_list:
    if word not in word_dict.keys():
      word_dict[word] = 1
    else:
      word_dict[word] += 1
  print(word_dict)


count_word_frequency('The sun rises in the east.')