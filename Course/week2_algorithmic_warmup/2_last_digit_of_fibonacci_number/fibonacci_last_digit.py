# Uses python3
import sys

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10


def get_fibonacci_last_digit_fast(n):
    fib1 = 0
    fib2 = 1
    for i in range(2, n+1):
        temp = fib2
        fib2 = (fib1 + fib2)%10
        fib1 = temp
    return fib2



if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
