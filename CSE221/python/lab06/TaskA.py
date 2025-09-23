from collections import deque

def advising(n,in_deg,graph):
    queue = deque()
    order = []
    for i in range(1,n+1):
        if(in_deg[i] == 0):
            queue.append(i)


    while queue:
        temp = queue.popleft()
        order.append(temp)
        for neighbour in graph[temp]:

            in_deg[neighbour] -=1
            if(in_deg[neighbour]==0):
                queue.append(neighbour)


    return order

n,m = map(int,input().split())
in_deg = [0]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    in_deg[e]+=1

order = advising(n,in_deg,graph)
if(len(order)==n):
    print(' '.join(map(str, order)))
else:
    print("-1")
