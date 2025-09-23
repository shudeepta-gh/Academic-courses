import heapq
def shortest_path(n,s,inf,graph):


    dis = [inf]*(n+1)
    dis[s]=0
    pq = [(dis[s], s)]
    while pq:
        dist_temp,temp = heapq.heappop(pq)
        for e,w in graph[temp]:
            if(dis[e]>dist_temp+w):
                dis[e] = dist_temp+w

                heapq.heappush(pq,(dis[e],e))

    return dis


n,m,s,t = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    s_point,e_point,weight = map(int,input().split())
    graph[s_point].append((e_point,weight))

inf = float('inf')
alice_dis = shortest_path(n,s,inf,graph)
bob_dis = shortest_path(n,t,inf,graph)


min_dis = inf
min_node = 0
for i in range(1,n+1):
    if(max(alice_dis[i] , bob_dis[i]) <min_dis):
        min_dis = max(alice_dis[i],bob_dis[i])
        min_node = i


if(min_dis==inf):
    print(-1)

else:
    print(min_dis,min_node)
