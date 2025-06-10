def compress_matrix(mat):

  rows,cols = mat.shape
  new_arr = np.zeros((2,2),dtype=int)

  for row in range(0,rows,2):

    for col in range(0,cols,2):
      sum = mat[row][col] + mat[row+1][col] + mat[row][col+1] + mat[row+1][col+1]

      for i in range(len(new_arr)):
        for j in range(len(new_arr[0])):
          if(new_arr[i][j] == 0):
            new_arr[i][j] = sum
            sum = 0

  return new_arr

matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------
