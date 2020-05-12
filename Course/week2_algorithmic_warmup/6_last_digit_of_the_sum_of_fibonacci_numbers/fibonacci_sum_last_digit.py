# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

def fibLastDigSum(n):
    fibLast = [0, 1]
    for i in range(2, n+1):
        fibLast.append((fibLast[i-1] + fibLast[i-2]) % 10) # Finds a repeating pattern in this case, 60
        if fibLast[-1] == 1 and fibLast[-2] == 0:
            fibLast = fibLast[:-2]
            break
    sumLast = sum(fibLast) % 10 # Last digit of the sum of first 60 numbers in 0
    return fibLast, sumLast

def fibonacci_sum_fast(n):
    lastDig, sumLast = fibLastDigSum(n)
    x = n % len(lastDig)
    y = n // (len(lastDig))
    sumTotal = y*sumLast + sum(lastDig[:x+1])
    return (sumTotal % 10)

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))
