
import sys
sys.setrecursionlimit(2*100000+5)


def dfs(i,vis,path_vis,adj_list):
    vis[i] = 1
    path_vis[i] = 1
    for j in adj_list[i-1]:
        if(vis[j]==0):
            if(dfs(j,visited,path_visited,adj_list)==True):
                return True


        elif(path_vis[j]==1):
            return True

    path_vis[i]=0
    return False


n,m = map(int, input().split())
adj_list =[[] for i in range(n)]
for i in range(m):
    s,e = map(int,input().split())
    adj_list[s-1].append(e)


visited = [0]*(n+1)
path_visited = [0]*(n+1)
hasCycle = False

for i in range(1,n+1):
    if(visited[i]==0):
        if(dfs(i,visited,path_visited,adj_list)==True):
            hasCycle = True
            break

if(hasCycle==True):
    print("YES")
else:
    print("NO")
