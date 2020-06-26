# Program to count character frequency in a string

input = input('Enter a string: ')
input = input.lower()
frequency = {}
for char in input:
  if char not in frequency.keys():
    frequency[char] = 1
  else:
    frequency[char] += 1

print(frequency)