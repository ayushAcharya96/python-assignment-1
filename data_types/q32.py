def generate_dict(n):
  return { n : n * n for n in range(1,n+1)}

print(generate_dict(5))