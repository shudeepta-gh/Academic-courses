import sys
sys.setrecursionlimit(2*10**6)

def diamond_collect(i,j,graph,visited,r,h):

    if(i<0 or j<0 or i>=r or j>=h):
        return 0

    if graph[i][j] == "#" or visited[i][j]:
        return 0

    visited[i][j] = 1
    if graph[i][j] == "D":
        count = 1

    else:
        count = 0


    count += diamond_collect(i-1,j,graph,visited,r,h)
    count += diamond_collect(i+1,j,graph,visited,r,h)
    count += diamond_collect(i,j-1,graph,visited,r,h)
    count += diamond_collect(i,j+1,graph,visited,r,h)

    return count


r,h = map(int, input().split())
graph = [[0]*h for i in range(r)]

for i in range(r):
    cells = input()
    for j in range(h):
        graph[i][j] = cells[j]

visited = [[0]*h for i in range(r)]
max_count = 0

for i in range(r):
    for j in range(h):
        if graph[i][j] != "#" and not visited[i][j]:
            count = diamond_collect(i,j, graph, visited, r, h)
            if count > max_count:
                max_count = count

print(max_count)
