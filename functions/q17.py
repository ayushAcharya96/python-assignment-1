starts_with_given_char = lambda string, char: str(string[0]).lower() == str(char).lower()

print(starts_with_given_char("Python", 'p'))
print(starts_with_given_char("apple", 'p'))
print(starts_with_given_char("23", 1))