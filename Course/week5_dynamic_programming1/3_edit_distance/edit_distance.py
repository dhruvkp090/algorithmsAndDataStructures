# Uses python3
def edit_distance(s, t):
    lens = len(s)
    lent = len(t)
    distance = [[0]*(lens + 1) for _ in range(lent + 1)]
    for i in range(lens + 1):
        distance[0][i] = i
    for i in range(lent + 1):
        distance[i][0] = i
    for j in range(1, lens + 1):
        for i in range(1, lent + 1):
            ins = distance[i][j - 1] + 1
            dele = distance[i - 1][j] + 1
            mis = distance[i-1][j-1] + 1
            mat = distance[i-1][j-1]
            if s[j - 1] == t[i - 1]:
                distance[i][j] = min(ins, dele, mat)
            else:
                distance[i][j] = min(ins, dele, mis)
    return distance[lent][lens]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
