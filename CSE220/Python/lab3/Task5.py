def play_game(arena):
  rows,cols = arena.shape
  count=0

  for i in range(rows):
    for j in range(cols):

      if(arena[i][j]%50==0 and arena[i][j]!=0):

        if(j<cols-1):
          if(arena[i][j+1]==2):
           count+=2

        if(j>0):
          if(arena[i][j-1]==2):
           count+=2

        if(i>0):
          if(arena[i-1][j]==2):
           count+=2
        if(i<rows-1):
          if(arena[i+1][j]==2):
           count+=2

  print(f"Points Gained: {count}.",end=" ")

  if(count>=10):
    print(f"Your team has survived the game.")

  else:
    print("Your team is out.")

arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)

print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
