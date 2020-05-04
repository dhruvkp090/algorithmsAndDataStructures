import ctypes
class DynamicArray():
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.A = self._makeArray(self.cap)

    /* Length of the array */
    def __len__(self):
        return self.n

    /* The object can we called as n array eg: out[k] */
    def __getitem__(self, k):
        if not 0<=k<self.n: // if the index is less than 0 or greater than n
            return IndexError("Index out of bounds")
        return self.A[k]

    /* Used to get index of an element in the array */
    def indexOf(self, ele):
        for i in range(self.n):
            if self.A[i] == ele:
                return i
        return -1
    /* The function used to addend or add an element in the array */
    def append(self, ele):
        if self.n == self.cap: // if the array is full
            self._resize(2*self.cap) // Double the capacity
            self.A[self.n] = ele
            self.n+=1
        else:
            self.A[self.n] = ele
            self.n+=1

    def _resize(self, newCap):
        temp = self._makeArray(newCap)
        for i in range(self.n):
            temp[i] = self.A[i] // Adding all of A elements in the the new array eith double the capacity
        self.A = temp // renaming temp to A
        self.cap = newCap // updating capacity

    def _makeArray(self, capacity):
        return (capacity*ctypes.py_object)() // Making array of size capacity

    /*Print all array elements */
    def printElements(self):
        for k in range(self.n):
            print(self.A[k])

out = DynamicArray()
