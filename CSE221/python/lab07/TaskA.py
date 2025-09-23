
import heapq
def shortest_path(n,s,d,graph):

    inf = float('inf')
    dis = [inf]*(n+1)
    parent = [-1]*(n+1)
    dis[s]=0
    pq = [(dis[s], s)]


    while pq:
        dist_temp,temp = heapq.heappop(pq)
        for e,w in graph[temp]:
            if(dis[e]>dist_temp+w):
                dis[e] = dist_temp+w
                parent[e] = temp
                heapq.heappush(pq,(dis[e],e))
    p=[]
    p.append(d)
    start = d
    while(parent[start]!=-1):
        p.append(parent[start])
        start = parent[start]
    if(len(p)==1 and d!=s):
        print(-1)

    else:
        print(dis[d])
        for i in range(len(p)-1,-1,-1):
            print(p[i],end=' ')


n,m,s,d = map(int,input().split())
graph = [[] for i in range(n+1)]
s_points = list(map(int,input().split()))
e_points = list(map(int,input().split()))
weights = list(map(int,input().split()))
for i in range(m):

    graph[s_points[i]].append((e_points[i],weights[i]))

shortest_path(n,s,d,graph)
