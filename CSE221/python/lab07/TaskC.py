
import heapq
def minimize_danger(n,graph):
    inf = float('inf')
    dis = [inf]*(n+1)
    dis[1] = 0
    pq = [(0,1)]
    while pq:
        danger,temp = heapq.heappop(pq)
        for e,w in graph[temp]:
            new_danger = max(danger,w)
            if(new_danger < dis[e]):
                dis[e] = new_danger
                heapq.heappush(pq,(dis[e],e))

    for i in range(1,len(dis)):
        if(dis[i]==inf):
            print(-1,end=' ')

        else:
            print(dis[i],end=' ')



n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))


minimize_danger(n,graph)

