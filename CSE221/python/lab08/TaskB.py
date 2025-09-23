
import sys
sys.setrecursionlimit(1_000_000)


def find_root(a, parent, size):
    if parent[a] != a:
        parent[a] = find_root(parent[a], parent, size)
    return parent[a]

def union(a, b, parent, size):
    root_A = find_root(a, parent, size)
    root_B = find_root(b, parent, size)

    if root_A != root_B:
        if size[root_B] > size[root_A]:
            parent[root_A] = root_B
            size[root_B] += size[root_A]
        else:
            parent[root_B] = root_A
            size[root_A] += size[root_B]

        return True
    return False

n,m = map(int,input().split())
edges = []
for i in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))

sorted_edge = sorted(edges)
size = [1]*(n+1)
parent = [i for i in range(n+1)]
total_cost = 0
for w,u,v in sorted_edge:
    if(union(u,v,parent,size)==True):
        total_cost+=w

print(total_cost)
