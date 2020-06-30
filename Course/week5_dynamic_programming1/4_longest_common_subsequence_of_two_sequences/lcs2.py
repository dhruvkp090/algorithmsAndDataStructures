#Uses python3

import sys

def lcs2(a, b):
    lena = len(a)
    lenb = len(b)
    distance = [[0]*(lena + 1) for _ in range(lenb + 1)]
    for i in range(lena + 1):
        distance[0][i] = 0
    for i in range(lenb + 1):
        distance[i][0] = 0
    for j in range(1, lena + 1):
        for i in range(1, lenb + 1):
            if a[j - 1] == b[i - 1]:
                distance[i][j] = distance[i - 1][j - 1] + 1
            else:
                distance[i][j] = max(distance[i - 1][j], distance[i][j - 1])
    return max(max(distance))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
