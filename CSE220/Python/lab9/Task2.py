#Using Matrix
def max_edge_weight(graph, vertices):

  row,col = graph.shape
  max_sum = 0
  max_vertex = " "
  for i in range(row):
    sum = 0
    for j in range(col):
      sum += graph[i][j]

    if(i == 0 or sum > max_sum):
       max_sum = sum
       max_vertex = vertices[i]

  return max_vertex

vertices = ['A','B','C','D','E','F','G']
graph = np.array([[1,2,4,9,0,0,0],
                  [2,0,13,3,8,16,0],
                  [4,13,0,10,0,11,5],
                  [9,3,10,0,6,7,14],
                  [0,8,0,6,0,12,0],
                  [0,16,11,7,12,0,15],
                  [0,0,5,14,0,15,0]]
                 )

print(max_edge_weight(graph, vertices))

#Using Linkedlist

class Graph:
  def __init__(self,elem,weight):
    self.elem = elem
    self.next = None
    self.weight = weight

def max_edge_weight(graph,vertices):
    max_sum = 0
    max_vertex = " "
    for i in range(len(graph)):
      sum = 0
      temp = graph[i]
      while(temp != None):
        sum += temp.weight
        temp = temp.next

      if(i == 0 or sum > max_sum):
        max_sum = sum
        max_vertex = vertices[i]


    return max_vertex



vertices = ['A','B','C','D','E','F','G']
graph = np.zeros(len(vertices),dtype = object)

graph[0] = Graph(vertices[0],1)
graph[0].next = Graph(vertices[1],2)
graph[0].next.next = Graph(vertices[2],4)
graph[0].next.next.next = Graph(vertices[3],9)

graph[1] = Graph(vertices[0],2)
graph[1].next = Graph(vertices[2],13)
graph[1].next.next = Graph(vertices[3],3)
graph[1].next.next.next = Graph(vertices[4],8)
graph[1].next.next.next.next= Graph(vertices[5],16)

graph[2] = Graph(vertices[0],4)
graph[2].next = Graph(vertices[1],13)
graph[2].next.next = Graph(vertices[3],10)
graph[2].next.next.next = Graph(vertices[5],11)
graph[2].next.next.next.next = Graph(vertices[6],5)

graph[3] = Graph(vertices[0],9)
graph[3].next = Graph(vertices[1],3)
graph[3].next.next = Graph(vertices[2],10)
graph[3].next.next.next = Graph(vertices[4],6)
graph[3].next.next.next.next= Graph(vertices[5],7)
graph[3].next.next.next.next.next= Graph(vertices[6],14)

graph[4] = Graph(vertices[1],8)
graph[4].next =Graph(vertices[3],6)
graph[4].next.next = Graph(vertices[5],12)

graph[5] = Graph(vertices[1],16)
graph[5].next = Graph(vertices[2],11)
graph[5].next.next = Graph(vertices[3],7)
graph[5].next.next.next = Graph(vertices[4],12)
graph[5].next.next.next.next= Graph(vertices[6],15)

graph[6] = Graph(vertices[2],5)
graph[6].next = Graph(vertices[3],14)
graph[6].next.next = Graph(vertices[5],15)

print(max_edge_weight(graph,vertices))


