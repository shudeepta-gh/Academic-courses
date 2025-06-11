def machine_process_time(tasks, m):

  arr = np.zeros(m, dtype = int)
  heap = MinHeap(m)

  for i in arr:
    heap.insert(i)


  for i in tasks:
    i = heap.extractMin()+i
    heap.insert(i)

  count = 0
  while(count<m):
    arr[count] = heap.extractMin()
    count+=1

  return arr

tasks = [2, 4, 7, 1, 6]
m = 4
print(machine_process_time(tasks, m))
