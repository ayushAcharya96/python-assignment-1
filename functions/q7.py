def is_upper(char):
  if char >= 'A' and char <= 'Z':
    return True
  return False

def is_lower(char):
  if char >= 'a' and char <= 'z':
    return True
  return False
def calculate_case_frequency(string):
  uppercase_frequency = 0
  lowercase_frequency = 0
  for char in string:
    if is_upper(char):
      uppercase_frequency += 1
    if is_lower(char):
      lowercase_frequency += 1
  print(f'In string : "{string}", Upper Case : {uppercase_frequency} and Lower Case : {lowercase_frequency}')

calculate_case_frequency('The quick Brown Fox')