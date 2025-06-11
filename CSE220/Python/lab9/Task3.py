#Using Matrix

def directed_edge_weighted(graph,vertices):
  row,col = graph.shape
  max_sum = 0
  max_deg = 0
  max_vertex = " "

  for i in range(row):
    sum = 0
    count = 0
    for j in range(col):
      sum += graph[i][j]
      if(graph[i][j] != 0):
         count += 1

    if(i==0 or count > max_deg):
       max_deg = count

    if(i==0 or sum > max_sum):
       max_sum = sum
       max_vertex = vertices[i]

  print(f"Maximum degree : {max_deg} \nMaximum edge weight : {max_sum}\nMaximum vertex: {max_vertex} ")

vertexes = ['A','B','C','D','E','F','G']
graph = np.array([[1,2,0,0,0,0,0],
                  [0,0,13,0,8,0,0],
                  [4,0,0,0,0,11,0],
                  [9,3,10,0,6,0,14],
                  [0,0,0,0,0,12,0],
                  [0,16,0,7,0,0,15],
                  [0,0,5,0,0,0,0]]
                 )

directed_edge_weighted(graph, vertexes)

#Using Linkedlist

class Graph:
  def __init__(self,start,end,weight):
    self.start = start
    self.end = end
    self.weight = weight
    self.next = None

def directed_edge_weighted(graph,vertices):

  max_sum = 0
  max_deg = 0
  max_vertex = " "

  for i in range (len(graph)):
    count = 0
    sum = 0
    temp = graph[i]
    while(temp!=None):
      count+=1
      sum += temp.weight
      temp = temp.next


    if(i==0 or count > max_deg):
       max_deg = count

    if(i==0 or sum > max_sum):
       max_sum = sum
       max_vertex = vertices[i]

  print(f"Maximum degree : {max_deg} \nMaximum edge weight : {max_sum}\nMaximum vertex: {max_vertex} ")


vertices = ['A','B','C','D','E','F','G']
graph = np.zeros(len(vertices),dtype = object)

graph[0] = Graph(vertices[0],vertices[0],1)
graph[0].next = Graph(vertices[0],vertices[1],2)


graph[1] = Graph(vertices[1],vertices[2],13)
graph[1].next = Graph(vertices[1],vertices[4],8)


graph[2] = Graph(vertices[2],vertices[0],4)
graph[2].next = Graph(vertices[2],vertices[5],11)


graph[3] = Graph(vertices[3],vertices[0],9)
graph[3].next = Graph(vertices[3],vertices[1],3)
graph[3].next.next = Graph(vertices[3],vertices[2],10)
graph[3].next.next.next = Graph(vertices[3],vertices[4],6)
graph[3].next.next.next.next= Graph(vertices[3],vertices[6],14)


graph[4] = Graph(vertices[4],vertices[5],12)

graph[5] = Graph(vertices[5],vertices[1],16)
graph[5].next = Graph(vertices[5],vertices[3],7)
graph[5].next.next = Graph(vertices[5],vertices[6],15)


graph[6] = Graph(vertices[6],vertices[2],5)

directed_edge_weighted(graph,vertices)

