def top_k_times_largest(arr, k):

  heap = MaxHeap(len(arr))
  result = np.zeros(k, dtype=int)
  for i in arr:
    heap.insert(i)
  count = 0
  while(count<k):
    result[count] = heap.extractMax()
    count+=1

  return result



nums = [4, 10, 2, 8, 6, 7]
k = int(input())


print(top_k_times_largest(nums, k))
