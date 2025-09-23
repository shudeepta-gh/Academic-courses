n,m = map(int, input().split())
count = [0 for i in range(n)]
s_points = list(map(int, input().split()))
e_points = list(map(int, input().split()))
for i in range(m):
    count[s_points[i]-1]+=1
    count[e_points[i]-1]+=1

counter = 0
for i in range(len(count)):
    if(count[i]%2!=0):
        counter+=1

if(counter==0 or counter==2):
    print("YES")

else:
    print("NO")
