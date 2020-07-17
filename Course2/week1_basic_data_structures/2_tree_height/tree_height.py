# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height
    tree = [[] for _ in range(n)]
    queue = []
    root = -1
    top = -1
    for i in range(len(parents)):
        if parents[i] != -1:
            tree[parents[i]].append(i)
        else:
            root = i

    queue.append(root)
    height = 0
    last = 0
    while queue:
        c = tree[queue.pop(0)]
        for b in c:
            queue.append(b)
            top +=1
            last = b
    while last != -1:
        height += 1
        last = parents[last]

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
