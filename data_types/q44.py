def slice_tuple(input_tuple, start=0, end=0):
  if start == 0 and end == 0:
    return input_tuple
  return input_tuple[start:end]

print(slice_tuple((1,2,3,4,5)))
print(slice_tuple((1,2,3,4,5), 2, 7))
print(slice_tuple((1,2,3,4,5),2 ,-2))