size = int(input())
x,y = map(int,input().split())
moves = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]

valid_move = []
for i in range(len(moves)):
    if(1<=moves[i][0]<=size and 1<=moves[i][1]<=size):
        valid_move.append(moves[i])

print(len(valid_move))
for i in range(len(valid_move)):
    print(" ".join(list(map(str,valid_move[i]))))
