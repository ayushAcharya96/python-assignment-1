def exchange_first_last_char(string):
  return f'{string[-1]}{string[1:-1]}{string[0]}'

print(exchange_first_last_char('happy'))
print(exchange_first_last_char('python'))