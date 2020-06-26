def filter_integer(iter):
  result_iter = list(filter(lambda x: (type(x) == int),iter))
  return result_iter

print(filter_integer([1,'a',1.2,34, 'hi', True, None]))