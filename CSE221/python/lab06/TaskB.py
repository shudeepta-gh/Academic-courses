
from collections import deque
def football_match(start,graph,color,ans):


        if(color[start]!=''):
          return ans

        queue = deque()
        queue.append(start)
        color[start] = "red"
        cnt_red,cnt_green = 1,0

        while queue:
            temp = queue.popleft()
            for neighbour in graph[temp]:
              if(color[neighbour]==''):

                  if(color[temp]=="red"):
                      color[neighbour]="green"
                      cnt_green +=1
                  else:
                      color[neighbour]="red"
                      cnt_red += 1

                  queue.append(neighbour)

              elif(color[neighbour]==color[temp]):
                  return -1

        ans+=max(cnt_red, cnt_green)
        return ans


n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

ans = 0
color = ['']*(n+1)
for i in range(1,n+1):
    ans = football_match(i,graph,color,ans)

print(ans)
