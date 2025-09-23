import sys
sys.setrecursionlimit(2*100000+5)
def dfs(node,visited,adj_list):
    visited[node] = 1
    print(str(node),end=" ")
    for i in adj_list[node-1]:
        if(visited[i]==0):
            dfs(i,visited,adj_list)




n,m = map(int, input().split())
s_points = list(map(int,input().split()))
e_points = list(map(int,input().split()))
adj_list = [[] for i in range(n)]
for i in range(m):
    adj_list[s_points[i]-1].append(e_points[i])
    adj_list[e_points[i]-1].append(s_points[i])

visited = [0]*(n+1)

dfs(1,visited,adj_list)
