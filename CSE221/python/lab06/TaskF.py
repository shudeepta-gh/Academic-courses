from collections import deque
def nearest_tour(n,sources,destinations,graph):
    dis = [-1]*(n+1)
    queue = deque()
    for i in sources:
        queue.append(i)
        dis[i] = 0

    while queue:
        temp = queue.popleft()
        for neighbour in graph[temp]:
            if(dis[neighbour]==-1):
                dis[neighbour] = dis[temp]+1
                queue.append(neighbour)

    for d in destinations:
        print(dis[d],end=' ')

n,m,s,q = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))
nearest_tour(n,sources,destinations,graph)
