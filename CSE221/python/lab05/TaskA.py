
from collections import deque
def Bfs(start,visited,adj_list):
    queue = deque()
    visited[start] = 1
    queue.append(start)
    order = []

    while queue:
        temp = queue.popleft()

        order.append(temp)
        for j in adj_list[temp-1]:
            if(visited[j]==0):
                queue.append(j)

                visited[j] = 1

    return order


n,m = map(int,input().split())
adj_list = [[] for i in range(n)]
for i in range(m):
    start,end = map(int,input().split())
    adj_list[start-1].append(end)
    adj_list[end-1].append(start)

visited = [0]*(n+1)


order = Bfs(1,visited,adj_list)
print(" ".join(map(str, order)))
