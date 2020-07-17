# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    slider = deque([], m)
    maximums = []
    window = m
    if (m == 1):
        return sequence
    for i in range(m):
        while len(slider) > 0 and sequence[i] > sequence[slider[0]]:
            slider.popleft()
        while len(slider) > 1 and sequence[i] > sequence[slider[-1]]:
            slider.pop()
        slider.append(i)
    for i in range(m , len(sequence)):
        maximums.append(sequence[slider[0]])
        while len(slider) > 0 and slider[0] <= (i - m):
            slider.popleft()
        while len(slider) > 0 and sequence[i] > sequence[slider[0]]:
            slider.popleft()
        while len(slider) > 1 and sequence[i] > sequence[slider[-1]]:
            slider.pop()
        slider.append(i)
    maximums.append(sequence[slider[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

