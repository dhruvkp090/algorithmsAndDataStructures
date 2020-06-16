# Uses python3
import sys

from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    a = zip(starts, [float('-inf')]*len(starts))
    b = zip(ends, [float('inf')]*len(ends))
    c = zip(points, range(len(points)))
    sortedlist = sorted(chain(a,b,c), key=lambda a : (a[0], a[1]))
    stack = []
    for i, j in sortedlist:
        if j == float('-inf'):
            stack.append(j)
        elif j == float('inf'):
            stack.pop()
        else:
            cnt[j] = len(stack)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
