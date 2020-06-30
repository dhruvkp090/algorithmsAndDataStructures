#Uses python3

import sys

def lcs3(a, b, c):
    lena = len(a)
    lenb = len(b)
    lenc = len(c)
    distance = [[[0]*(lena + 1) for _ in range(lenb + 1)]for _ in range(lenc + 1)]
    for k in range(1, lena + 1):
        for j in range(1, lenb + 1):
            for i in range(1, lenc + 1):
                if a[k - 1] == b[j - 1] and b[j - 1] == c[i - 1]:
                    distance[i][j][k] = distance[i - 1][j - 1][k - 1] + 1
                else:
                    distance[i][j][k] = max(distance[i - 1][j][k], distance[i][j - 1][k], distance[i][j][k - 1])
    return max(max(max(distance)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
