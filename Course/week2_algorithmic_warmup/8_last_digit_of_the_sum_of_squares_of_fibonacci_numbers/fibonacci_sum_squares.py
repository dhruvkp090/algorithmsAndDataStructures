# Uses python3
from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10
def FibLastDig(m):
    fibLast = [0, 1]
    for i in range(2, m+1):
        fibLast.append((fibLast[i-1] + fibLast[i-2]) % 10) # Finds a repeating pattern in this case, 60
        if fibLast[-1] == 1 and fibLast[-2] == 0:
            fibLast = fibLast[:-2]
            break
    return fibLast


def fibonacci_sum_squares_fast(n):
    fibLast = FibLastDig(n+1)

    x = n % len(fibLast)
    y = (n+1) % len(fibLast)

    return (fibLast[x]* fibLast[y]) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
