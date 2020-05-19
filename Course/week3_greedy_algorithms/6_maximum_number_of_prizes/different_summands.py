# Uses python3
import sys

def optimal_summands(n):
    summands = []
    currMax = 1
    updateN = n
    #write your code here
    for i in range(1, n+1):
        if (updateN - i) > i:
            summands.append(i)
            updateN -= i
        else:
            summands.append(updateN)
            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
