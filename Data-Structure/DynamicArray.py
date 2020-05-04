import ctypes
class DynamicArray():
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.A = self._makeArray(self.cap)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0<=k<self.n:
            return IndexError("Index out of bounds")
        return self.A[k]

    def indexOf(self, ele):
        for i in range(self.n):
            if self.A[i] == ele:
                return i
        return -1

    def append(self, ele):
        if self.n == self.cap:
            self._resize(2*self.cap)
            self.A[self.n] = ele
            self.n+=1
        else:
            self.A[self.n] = ele
            self.n+=1

    def _resize(self, newCap):
        temp = self._makeArray(newCap)
        for i in range(self.n):
            temp[i] = self.A[i]
        self.A = temp
        self.cap = newCap

    def _makeArray(self, capacity):
        return (capacity*ctypes.py_object)()

    def printElements(self):
        for k in range(self.n):
            print(self.A[k])

out = DynamicArray()
