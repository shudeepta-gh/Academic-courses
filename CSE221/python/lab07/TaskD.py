
import heapq
def beautiful_path(n,s,d,weights,graph):
    inf = float('inf')
    cost = [inf]*(n+1)
    cost[s] = weights[s-1]
    pq = [(cost[s],s)]

    while pq:
        temp_cost,temp = heapq.heappop(pq)
        for nei in graph[temp]:
            if(temp_cost+weights[nei-1] < cost[nei]):
                cost[nei] = temp_cost + weights[nei-1]

                heapq.heappush(pq,(cost[nei],nei))

    if(cost[d]!=inf):
       print(cost[d])

    else:
        print(-1)


n,m,s,d = map(int,input().split())
node_weights = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
for i in range(m):
    s_p,e_p = map(int,input().split())
    graph[s_p].append(e_p)


beautiful_path(n,s,d,node_weights,graph)
