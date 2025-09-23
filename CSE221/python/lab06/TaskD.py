
from collections import deque
def longest_path_find(start,n,graph):
    dis = [-1]*(n+1)
    queue = deque()
    queue.append(start)
    dis[start]=0
    farthest_node = start
    while queue:
        temp = queue.popleft()
        for neighbour in graph[temp]:
            if(dis[neighbour]==-1):
                dis[neighbour] = dis[temp]+1
                queue.append(neighbour)
                if(dis[farthest_node]<dis[neighbour]):
                    farthest_node = neighbour


    return farthest_node, dis[farthest_node]


n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

node_A, one_to_A = longest_path_find(1,n,graph)
node_B, A_to_B = longest_path_find(node_A,n,graph)
print(A_to_B)
print(node_A,node_B)
