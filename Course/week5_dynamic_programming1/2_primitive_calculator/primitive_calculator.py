# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    operations = [-1, 0, 1, 1, 2]
    for i in range(5, n + 1):
        div3 = 0
        div2 = 0
        if i % 3 == 0:
            div3 = i //3
            operations.append(min(operations[i - 1] + 1,operations[div3] + 1))
        elif i % 2 == 0:
            div2 = i // 2
            operations.append(min(operations[i - 1] + 1,operations[div2] + 1))
        else:
            operations.append(operations[i - 1] + 1)
    sequence.append(n)
    while n > 1:
        if n % 3 == 0:
            div3 = n //3
            if operations[n-1] <= operations[div3]:
                n = n - 1
                sequence.append(n)
            else:
                n = n //3
                sequence.append(n)
        elif n % 2 == 0:
            div2 = n //2
            if operations[n-1] <= operations[div2]:
                n = n - 1
                sequence.append(n)
            else:
                n = n //2
                sequence.append(n)
        else:
            n = n-1
            sequence.append(n)
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
