from collections import deque
def Bfs(s,d,parent,dis,adj_list):
    queue  = deque()
    dis[s] = 0
    queue.append(s)
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

n,m,s,d = map(int, input().split())
adj_list = [[] for i in range(n)]
s_points = list(map(int, input().split()))
e_points = list(map(int, input().split()))
for i in range(m):
    adj_list[s_points[i]-1].append(e_points[i])
    adj_list[e_points[i]-1].append(s_points[i])

for i in range(n):
    adj_list[i] = sorted(adj_list[i])

INF = float('inf')
dis = [INF]*(n+1)
parent = [-1]*(n+1)

path = Bfs(s,d,parent,dis,adj_list)
if(path!=-1):
    print(len(path)-1)
    print(' '.join(map(str, path)))
else:
    print(str(path))
