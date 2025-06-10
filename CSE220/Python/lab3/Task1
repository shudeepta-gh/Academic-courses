def walk_zigzag(floor):
  row,col = floor.shape

  for j in range(col):
    if(j%2==0):
      for i in range(0,row,2):
         print(floor[i][j],end=" ")

      print()
    else:
      if(row==col):

        for i in range(row-2,-1,-2):
           print(floor[i][j],end=" ")


      elif(row<col):
        for i in range(row-1,-1,-2):
           print(floor[i][j],end=" ")
      print()



floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8
