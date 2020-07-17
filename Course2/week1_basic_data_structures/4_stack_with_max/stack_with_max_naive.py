#python3
import sys
from collections import deque

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maxAtEachPush = deque([])
        self.pushCount = 0

    def Push(self, a):
        self.__stack.append(a)
        if self.pushCount == 0:
            self.maxAtEachPush.append(a)
            self.pushCount += 1
        else:
            self.maxAtEachPush.append(max(a, self.maxAtEachPush[-1]))
            self.pushCount += 1

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.pushCount -= 1

    def Max(self):
        assert(len(self.__stack))
        return self.maxAtEachPush[self.pushCount - 1]



if __name__ == '__main__':
    stack = StackWithMax()
    output = []
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            output.append(stack.Max())
        else:
            assert(0)
    for o in output:
        print(o)
