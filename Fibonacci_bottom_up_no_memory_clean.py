# Choose the position to calculate it's value
p = 44

# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = [
            0,
            1
        ]
        for i in range(2, n + 1):
            temp.append(temp[i - 1] + temp[i - 2])
        return temp[n]

# Make time and memory test
import time
import sys

def fibonacci_mu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = [
            0,
            1
        ]
        for i in range(2, n + 1):
            temp.append(temp[i - 1] + temp[i - 2])
        return sys.getsizeof(temp)

for i in range(p + 1):
    t1 = time.time()
    print('fibonacci({}): {}'.format(i, fibonacci(i)))
    t2 = time.time()
    print("Time taken for n = {}: {} seconds".format(i, t2 - t1))
    print("Memory usage for the list: {} bytes".format(fibonacci_mu(i)))
    print('-' * 60)