
import sys
sys.setrecursionlimit(2*100000+5)

def dfs(root, visited, subtree, adj_list):
    visited[root] = 1
    subtree[root] = 1

    for neighbour in adj_list[root-1]:
        if visited[neighbour] == 0:
            dfs(neighbour, visited, subtree, adj_list)
            subtree[root] += subtree[neighbour]
    return subtree


n, root = map(int, input().split())
adj_list = [[] for i in range(n)]
for _ in range(n-1):
    s, e = map(int, input().split())
    adj_list[s-1].append(e)
    adj_list[e-1].append(s)

visited = [0] * (n+1)
subtree = [0] * (n+1)


subtree = dfs(root, visited, subtree, adj_list)

q = int(input())
q_list = []
for _ in range(q):
    x = int(input())
    q_list.append(subtree[x])

for i in q_list:
    print(i)
