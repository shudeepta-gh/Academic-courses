import numpy as np
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest


def mergeSortedArray(arr1, arr2):

  arr1_size=arr1.size
  arr2_size=arr2.size
  arr3=np.zeros((arr1_size+arr2_size),dtype=int)
  for i in range(arr1_size):
    arr3[i]=arr1[i]

  for i in range(arr2_size):
    arr3[i+arr1_size]=arr2[i]

  for i in range(arr3.size-1):
    for j in range(arr3.size-i-1):
      if(arr3[j]>arr3[j+1]):
        temp=arr3[j]
        arr3[j]=arr3[j+1]
        arr3[j+1]=temp

  return arr3





a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))
