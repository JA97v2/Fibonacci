# Choose the position to calculate it's value
p = 44

# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Make time test
import time

for i in range(p + 1):
    t1 = time.time()
    print('fibonacci({}): {}'.format(i, fibonacci(i)))
    t2 = time.time()
    print("Time taken for n = {}: {} seconds".format(i, t2 - t1))
    print('-' * 60)