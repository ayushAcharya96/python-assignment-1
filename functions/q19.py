fibonacci_series = lambda x: x if x == 1 else x + fibonacci_series(x-1)

print(fibonacci_series(10))
