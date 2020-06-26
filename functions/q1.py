def find_max(a, b, c):
  if a > b:
    if a > c:
      return a
    else:
      return c
  elif b > c:
    return b
  else:
    return c

print(find_max(1,2,3))
print(find_max(2,5,3))
print(find_max(3,1,2))
