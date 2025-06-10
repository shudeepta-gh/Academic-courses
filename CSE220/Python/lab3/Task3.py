def row_rotation(exam_week, seat_status):
  row,col = seat_status.shape

  for i in range(exam_week-1):
    last_row=np.zeros(col,dtype=object)

    for elem in range(len(last_row)):
        last_row[elem]=seat_status[row-1][elem]



    for i in range(row-1,0,-1):

        for j in range(col):
            seat_status[i][j] = seat_status[i-1][j]


    for k in range(col):
        seat_status[0][k] = last_row[k]



  print_matrix(seat_status)

  for i in range(row):
    for j in range(col):
      if(seat_status[i][j]=="AA"):
        return i+1


seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status)
print(f'Your friend AA will be on row {row_number}')
