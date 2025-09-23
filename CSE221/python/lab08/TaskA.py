
import sys
sys.setrecursionlimit(1_000_000)


def find_root(a,parent,size):

    if(parent[a]!=a):
        parent[a] = find_root(parent[a],parent,size)
    return parent[a]


def union(a,b,parent,size):
    root_A = find_root(a,parent,size)
    root_B = find_root(b,parent,size)

    if(root_A!=root_B):
        if(size[root_B]>size[root_A]):
            parent[root_A] = root_B
            size[root_B]+=size[root_A]
            return size[root_B]

        else:
            parent[root_B] = root_A
            size[root_A]+=size[root_B]
            return size[root_A]

    return size[root_A]



n,m = map(int, input().split())
parent= [i for i in range(n+1)]
size = [1]*(n+1)

for _ in range(m):
    x,y = map(int, input().split())
    print(union(x,y,parent,size))
