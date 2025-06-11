#Using Matrix

def max_degree(graph):
  row,col = graph.shape
  max_deg = 0
  for i in range(row):
    count = 0
    for j in range(col):
      if(graph[i][j] == 1):
         count += 1
    if(count > max_deg):
      max_deg = count


  return max_deg


graph = np.array([[1,1,1,1,0,0,0],
                  [1,0,1,1,1,1,0],
                  [1,1,0,1,0,1,1],
                  [1,1,1,0,1,1,1],
                  [0,1,0,1,0,1,0],
                  [0,1,1,1,1,0,1],
                  [0,0,1,1,0,1,0]]
                 )

print(max_degree(graph))



#Using Linkedlist

class Graph:
  def __init__(self,elem):
    self.elem = elem
    self.next = None

def max_degree(graph):
   max_deg = 0
   for i in range(len(graph)):
     count = 0
     temp = graph[i]
     while(temp!= None):
        count += 1
        temp = temp.next

     if(i == 0 or count > max_deg):
        max_deg = count

   return max_deg


vertices = ['A','B','C','D','E','F','G']
for i in range(len(vertices)):
  vertices[i] = Graph(vertices[i])

graph = np.zeros(len(vertices),dtype = object)
graph[0] = vertices[0]
graph[0].next = vertices[1]
graph[0].next.next = vertices[2]
graph[0].next.next.next = vertices[3]

graph[1] = vertices[0]
graph[1].next = vertices[2]
graph[1].next.next = vertices[3]
graph[1].next.next.next = vertices[4]
graph[1].next.next.next.next= vertices[5]

graph[2] = vertices[0]
graph[2].next = vertices[1]
graph[2].next.next = vertices[3]
graph[2].next.next.next = vertices[5]
graph[2].next.next.next.next = vertices[6]

graph[3] = vertices[0]
graph[3].next = vertices[1]
graph[3].next.next = vertices[2]
graph[3].next.next.next = vertices[4]
graph[3].next.next.next.next= vertices[5]
graph[3].next.next.next.next.next= vertices[6]

graph[4] = vertices[1]
graph[4].next = vertices[3]
graph[4].next.next = vertices[5]

graph[5] = vertices[1]
graph[5].next = vertices[2]
graph[5].next.next = vertices[3]
graph[5].next.next.next = vertices[4]
graph[5].next.next.next.next= vertices[6]

graph[6] = vertices[2]
graph[6].next = vertices[3]
graph[6].next.next = vertices[5]

print(max_degree(graph))
