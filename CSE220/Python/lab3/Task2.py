def decrypt_matrix(matrix):
  row,col = matrix.shape
  new_arr = np.zeros(col-1,dtype=int)

  for j in range(col-1):
    sum1 = 0
    sum2 = 0
    for i in range(row):
      sum1 += matrix[i][j]
      sum2 += matrix[i][j+1]

    result = sum2-sum1

    new_arr[j] = result

  return new_arr

matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
