# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while segments:
        removeList = []
        segments = sorted(segments, key = lambda x: x.end)
        points.append(segments[0][1])
        for s in segments:
            if points[-1] >= s.start and points[-1] <= s.end:
                removeList.append(s)
        segments = [x for x in segments if x not in removeList]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
