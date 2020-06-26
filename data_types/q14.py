def add_tags(tag, string):
  return f'<{tag}>{string}</{tag}>'

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorials'))
