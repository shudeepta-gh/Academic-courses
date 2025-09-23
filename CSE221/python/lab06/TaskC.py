
from collections import deque
def min_moves_needed(n,x1,y1,x2,y2):
    if((x1,y1)==(x2,y2)):
        return 0
    x_moves = [-2,-2,1,-1,1,-1,2,2]
    y_moves = [1,-1,2,2,-2,-2,1,-1]

    dis = [[-1]*(n+1) for i in range(n+1)]
    queue = deque()
    queue.append((x1,y1))
    dis[x1][y1]=0

    while queue:
        x1,y1 = queue.popleft()
        for i in range(8):
            x,y = x1+x_moves[i],y1+y_moves[i]
            if(1<=x<=n and 1<=y<=n and dis[x][y]==-1):

                dis[x][y] = dis[x1][y1]+1
                if((x,y)==(x2,y2)):
                    return dis[x][y]

                queue.append((x,y))

    return -1

n = int(input())
x1,y1,x2,y2 = map(int,input().split())
print(min_moves_needed(n,x1,y1,x2,y2))
