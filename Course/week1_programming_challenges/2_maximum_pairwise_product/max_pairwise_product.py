# python3
from numpy.random import randint
import numpy as np

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_faster(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_faster(input_numbers))
    """
    Stress Test code below

    """
    # while True:
    #     input_n = randint(0, 1000)
    #     input_numbers = randint(0, 10000, input_n)
    #     fast = max_pairwise_product_fast(input_numbers)
    #     brute = max_pairwise_product(input_numbers)
    #     if fast == brute:
    #         print(str(fast) + " " + str(brute))
    #         print(input_numbers)
    #         print("OK")
    #     else:
    #         print(str(fast) + " " + str(brute))
    #         print(input_numbers)
    #         print("ERROR!!")
    #         break

