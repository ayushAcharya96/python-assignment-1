def merge_dict(dict1, dict2):
  return {**dict1, **dict2}

print(merge_dict({1:10, 2:20}, {'a':'abc', 'x':'xyz'}))