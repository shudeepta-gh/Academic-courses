
import heapq
def second_shortest_path(n,s,d,graph):

    inf = float('inf')
    first = [inf]*(n+1)
    second = [inf]*(n+1)
    pq = [(0,s)]

    first[s] = 0
    while pq:
        cost,temp = heapq.heappop(pq)
        for e,w in graph[temp]:

            cand = cost + w

            if cand < first[e]:
               second[e] = first[e]
               first[e] = cand
               heapq.heappush(pq,(first[e],e))

            elif first[e] < cand < second[e]:
                second[e] = cand
                heapq.heappush(pq,(second[e],e))

    if(second[d] != inf):
        print(second[d])
    else:
        print(-1)


n,m,s,d = map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

second_shortest_path(n,s,d,graph)
