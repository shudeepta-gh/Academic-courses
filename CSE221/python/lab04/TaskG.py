n,m,k = map(int,input().split())
knights = set()
for i in range(k):
    x,y = map(int,input().split())
    knights.add((x,y))



can_attack = False
for x,y in knights:

    moves = [[x-2,y-1],[x-2,y+1],[x+1,y-2],[x-1,y-2],[x+2,y+1],[x+2,y-1],[x+1,y+2],[x-1,y+2]]
    for i,j in moves:
            if (i,j) in knights:

               can_attack = True
               break
    if(can_attack==True):
         break

if(can_attack == True):
    print("YES")
else:
    print("NO")
