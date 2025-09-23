
import heapq
def parity_edges(n,graph):
    inf = float('inf')
    dis = [[inf, inf] for i in range(n+1)]
    dis[1][0] = dis[1][1] = 0

    pq = [(0,1,-1)]

    while pq:
        dist,node,last_parity = heapq.heappop(pq)
        for end,weight in graph[node]:
            p = weight%2
            if(last_parity==-1 or p != last_parity):
                if(dist + weight < dis[end][p]):
                    dis[end][p] = dist+weight
                    heapq.heappush(pq,(dis[end][p],end,p))
    res = min(dis[n][0],dis[n][1])
    if(res!=inf):
       print(res)

    else:
        print(-1)


n,m = map(int, input().split())
s_points = list(map(int, input().split()))
e_points = list(map(int, input().split()))
weights = list(map(int, input().split()))
graph = [[] for i in range(n+1)]

for i in range(m):
    graph[s_points[i]].append((e_points[i],weights[i]))

parity_edges(n,graph)
