# Uses python3
import sys

def get_majority_element(a, left, right):
    a.sort()
    mid = (left + right)//2
    median = a[mid]
    count = 0
    for i in range(right):
        if a[i] == median:
            count += 1
    if count > right // 2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
