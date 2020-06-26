def is_in_range(number, start, end):
  if start <= end and number >= start and number <= end:
    return True
  elif start >= end and number <= start and number >= end:
      return True
  else:
    return False

print(is_in_range(5,1,7))
print(is_in_range(5,9,8))
print(is_in_range(-5,1,-7))