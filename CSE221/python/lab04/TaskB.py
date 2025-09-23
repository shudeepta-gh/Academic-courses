def adj_list_represenation(adj_list,start,end,weight):
    e_w = [end,weight]

    adj_list[start-1].append(tuple(e_w))

N,M = map(int,input().split(" "))
s_points = list(map(int,input().split(" ")))
e_points = list(map(int,input().split(" ")))
weights = list(map(int,input().split(" ")))

adj_list =  [[] for i in range(N)]


for i in range(M):
    adj_list_represenation(adj_list,s_points[i],e_points[i],weights[i])

for i in range(len(adj_list)):
    print(i+1 ,": "," ".join(map(str,adj_list[i])))
