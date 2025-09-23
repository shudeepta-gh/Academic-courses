
import math

n,q = map(int,input().split())
G = [[] for i in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and math.gcd(i,j)==1:
            G[i-1].append(j)

quaries = []
for i in range(q):
    x,y = map(int,input().split())
    quaries.append((x,y))

for x,y in quaries:
    if(y<=len(G[x-1])):
        print(G[x-1][y-1])

    else:
        print(-1)
