# python3
swaps = []
def leftChild(a):
    return (2*(a+1) - 1)

def rightChild(a):
    return (2*(a+1))

def shiftDown(data, a):
    size = len(data)
    minInd = a
    L = leftChild(a)
    if L < size and data[L] < data[minInd]:
        minInd = L
    R = rightChild(a)
    if R < size and data[R] < data[minInd]:
        minInd = R
    if a != minInd:
        temp = data[a]
        data[a] = data[minInd]
        data[minInd] = temp
        swaps.append((a, minInd))
        shiftDown(data, minInd)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    size = len(data)
    for i in range(size//2, -1,-1):
        shiftDown(data, i)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
