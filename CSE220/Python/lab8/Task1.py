class MinHeap:
  def __init__(self , capacity):

    self.__arr = np.zeros(capacity, dtype = int)
    self.__size = 0


  def getarray(self):
    return self.__arr



  def insert(self , key):
    if(self.__size < self.__arr.size):
       self.__arr[self.__size] = key
       idx = self.__size
       self.__size += 1
       self.swim(idx)

  def swim(self,idx):
    parent_idx = idx//2
    while(idx > 0 and self.__arr[idx] < self.__arr[parent_idx]):
      temp = self.__arr[idx]
      self.__arr[idx] = self.__arr[parent_idx]
      self.__arr[parent_idx] = temp
      idx = parent_idx
      parent_idx = idx//2

  def extractMin(self):

    if self.__size == 0:
        return None

    min_val = self.__arr[0]
    self.__size -= 1
    self.__arr[0] = self.__arr[self.__size]
    self.__arr[self.__size] = 0
    self.sink(0)
    return min_val



  def sink(self,idx):
    while True:
      left = idx*2
      right = idx*2+1
      smallest = idx
      if(left<self.__size and self.__arr[left]<self.__arr[smallest]):
        smallest = left
      if(right<self.__size and self.__arr[right]<self.__arr[smallest]):
        smallest = right

      if(smallest == idx):
        break
      temp = self.__arr[smallest]
      self.__arr[smallest] = self.__arr[idx]
      self.__arr[idx] = temp
      idx = smallest

  def sort(self):

    sorted_array = np.zeros(self.__size, dtype=int)
    ori_size = self.__size

    for i in range(ori_size):
        sorted_array[i] = self.extractMin()

    return sorted_array

heap = MinHeap(7)
heap.insert(50)
heap.insert(40)
heap.insert(35)
heap.insert(32)
heap.insert(70)

print(heap.sort())
