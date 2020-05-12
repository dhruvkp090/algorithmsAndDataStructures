# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10

def fibLastDigSum(n):
    fibLast = [0, 1]
    for i in range(2, n+1):
        fibLast.append((fibLast[i-1] + fibLast[i-2]) % 10) # Finds a repeating pattern in this case, 60
        if fibLast[-1] == 1 and fibLast[-2] == 0:
            fibLast = fibLast[:-2]
            break
    #sumLast = sum(fibLast) % 10 # Last digit of the sum of first 60 numbers in 0
    return fibLast

def fibonacci_partial_sum_fast(from_, to):
    lastDig = fibLastDigSum(to)
    x1 = from_ % len(lastDig)

    x2 = to % len(lastDig)

    sumTotal =  sum(lastDig[:x2+1]) - sum(lastDig[:x1])

    return (sumTotal % 10)


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))