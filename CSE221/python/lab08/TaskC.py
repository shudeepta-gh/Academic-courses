
import sys
sys.setrecursionlimit(1_000_000)

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def merge_sets(a, b, parent, size):
    root_a = find_parent(a, parent)
    root_b = find_parent(b, parent)
    if root_a == root_b:
        return False
    if size[root_a] < size[root_b]:
        parent[root_a] = root_b
        size[root_b] += size[root_a]
    else:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    return True

def build_mst(num_nodes, edge_list, blocked_edge=None, forced_edge=None):
    parent = [i for i in range(num_nodes + 1)]
    size = [1] * (num_nodes + 1)
    mst_weight = 0
    mst_edges = []

    if forced_edge is not None:
        w, u, v = edge_list[forced_edge]
        if merge_sets(u, v, parent, size):
            mst_weight += w
            mst_edges.append((w, u, v))
        else:
            return float('inf'), []

    for idx, (w, u, v) in enumerate(edge_list):
        if idx == blocked_edge or idx == forced_edge:
            continue
        if merge_sets(u, v, parent, size):
            mst_weight += w
            mst_edges.append((w, u, v))


    root = find_parent(1, parent)
    for i in range(2, num_nodes + 1):
        if find_parent(i, parent) != root:
            return float('inf'), mst_edges

    return mst_weight, mst_edges


nodes, edges_count = map(int, input().split())
edges = [tuple(map(int, input().split()))[::-1] for _ in range(edges_count)]
edges.sort()


min_weight, min_mst_edges = build_mst(nodes, edges)

second_best = float('inf')


for i, edge in enumerate(edges):
    if edge in min_mst_edges:
        weight, _ = build_mst(nodes, edges, blocked_edge=i)
        if weight > min_weight:
            second_best = min(second_best, weight)

min_mst_set = set(min_mst_edges)
for i, edge in enumerate(edges):
    if edge not in min_mst_set:
        weight, _ = build_mst(nodes, edges, forced_edge=i)
        if weight > min_weight:
            second_best = min(second_best, weight)

if second_best == float('inf'):
    print(-1)
else:
    print(second_best)
