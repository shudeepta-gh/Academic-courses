
n,m = map(int, input().split())
s_points = list(map(int, input().split()))
e_points = list(map(int, input().split()))
in_deg = [0 for i in range(n)]
out_deg = [0 for i in range(n)]
difference = []
for i in range(m):
    out_deg[s_points[i]-1]+=1
    in_deg[e_points[i]-1]+=1

for j in range(n):
    difference.append(str(in_deg[j]-out_deg[j]))

print(" ".join(difference))
