
from collections import deque
def Bfs(s,d,n,adj_list):
    queue  = deque()
    INF = float('inf')
    dis = [INF]*(n+1)
    parent = [-1]*(n+1)
    queue.append(s)
    dis[s] = 0
    while queue:
        temp = queue.popleft()
        for j in adj_list[temp-1]:
            if(dis[j]>dis[temp]+1):
                queue.append(j)
                dis[j] = dis[temp]+1
                parent[j] = temp

    if(dis[d] == INF):
        return -1
    p = d
    r_path = []
    while(p!=-1):
        r_path.append(p)
        p = parent[p]

    path = []
    for i in range(len(r_path)-1,-1,-1):
        path.append(r_path[i])


    return path

n,m,s,d,k = map(int,input().split())
adj_list = [[] for i in range(n)]
for i in range(m):
    start,end = map(int, input().split())
    adj_list[start-1].append(end)


s_to_k = Bfs(s,k,n,adj_list)
k_to_d = Bfs(k,d,n,adj_list)
if(s_to_k==-1 or k_to_d==-1):
    print(-1)


else:
    s_to_d = s_to_k + k_to_d

    for i in range(len(s_to_d)-1):
        if(s_to_d[i]==s_to_d[i+1]):
          del s_to_d[i]
          break

    print(len(s_to_d)-1)
    print(' '.join(map(str, s_to_d)))
