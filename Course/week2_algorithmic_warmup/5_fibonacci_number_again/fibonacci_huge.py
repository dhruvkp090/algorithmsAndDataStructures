# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


def pisanoPeriod(n, m):
    period = [0, 1]
    fib1 = 0
    fib2 = 1
    for i in range(2, n+1):
        temp = fib2
        fib2 = (fib1 + fib2) % m
        fib1 = temp
        if fib1 == 0 and fib2 == 1:
            break
        else:
            period.append(fib2)
    return period



def get_fibonacci_huge_fast(n, m):
    period = pisanoPeriod(n, m)
    if period[-1] == 0:
        x = n % (len(period) - 1)
    else:
        x = n % len(period)
    return period[x]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_fast(n, m))
