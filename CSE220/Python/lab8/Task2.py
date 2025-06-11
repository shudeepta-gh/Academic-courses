class MaxHeap:
    def __init__(self, capacity):
        self.__arr = np.zeros(capacity, dtype=int)
        self.__size = 0

    def getarray(self):
        return self.__arr

    def insert(self, key):
        if self.__size < self.__arr.size:
            self.__arr[self.__size] = key
            idx = self.__size
            self.__size += 1
            self.swim(idx)

    def swim(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.__arr[idx] > self.__arr[parent_idx]:
            self.__arr[idx], self.__arr[parent_idx] = self.__arr[parent_idx], self.__arr[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def extractMax(self):
        if self.__size == 0:
            return None

        max_val = self.__arr[0]
        self.__size -= 1
        self.__arr[0] = self.__arr[self.__size]
        self.__arr[self.__size] = 0
        self.sink(0)
        return max_val

    def sink(self, idx):
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < self.__size and self.__arr[left] > self.__arr[largest]:
                largest = left
            if right < self.__size and self.__arr[right] > self.__arr[largest]:
                largest = right

            if largest == idx:
                break

            temp = self.__arr[largest]
            self.__arr[largest] = self.__arr[idx]
            self.__arr[idx] = temp
            idx = largest


    def sort(self):
        sorted_array = np.zeros(self.__size, dtype=int)
        ori_size = self.__size

        for i in range(ori_size):
            sorted_array[i] = self.extractMax()


        return sorted_array


heap = MaxHeap(7)
heap.insert(50)
heap.insert(40)
heap.insert(35)
heap.insert(32)
heap.insert(70)


print(heap.sort())
