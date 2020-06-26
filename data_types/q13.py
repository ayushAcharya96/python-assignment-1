string_list = ['red', 'white', 'black', 'red', 'green', 'black']
string_list = list(dict.fromkeys(string_list))
string_list.sort()
print(string_list)

