# Uses python3
import sys

def get_change(m):
    availableCoins = [1, 3, 4]
    change = [0, 1,2,1,1]
    for i in range(5, m + 1):
        change.append(min(change[i - availableCoins[0]] + 1,\
                            change[i - availableCoins[1]] + 1, \
                            change[i - availableCoins[2]] + 1 ))
    return change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
