#Using Matrix

def converting_graph(graph,vertices):
  row,col = graph.shape
  for i in range(row):
    for j in range(col):
      if(graph[i][j] == 0 and graph[j][i] != 0):
        graph[i][j] = graph[j][i]

      elif(graph[j][i] == 0 and graph[i][j] != 0):
        graph[j][i] = graph[i][j]


  return graph


vertices = ['A','B','C','D','E','F','G']

graph = np.array([[1,2,0,0,0,0,0],
                  [0,0,13,0,8,0,0],
                  [4,0,0,0,0,11,0],
                  [9,3,10,0,6,0,14],
                  [0,0,0,0,0,12,0],
                  [0,16,0,7,0,0,15],
                  [0,0,5,0,0,0,0]]
                 )
print(converting_graph(graph, vertices))

#using Linkedlist

class Graph:
  def __init__(self,start,end,weight):
    self.start = start
    self.end = end
    self.weight = weight
    self.next = None

def add_edges(graph,idx,new_edge):
    if graph[idx] == None:
        graph[idx] = new_edge
    else:
        temp = graph[idx]
        while(temp.next!=None):
          temp = temp.next
        temp.next = new_edge

def converting_graph(graph, vertices):

    for i in range(len(graph)):
        temp = graph[i]
        while temp:
            if temp.start == temp.end:
                temp = temp.next
                continue
            count = 0
            for vertex in vertices:
                if temp.end == vertex:
                    break
                count += 1

            check = graph[count]
            exists = False
            while check!=None:
                if check.end == temp.start and check.start == temp.end and check.weight == temp.weight:
                    exists = True
                    break
                check = check.next

            if exists==False:
                new_edge = Graph(temp.end, temp.start, temp.weight)
                add_edges(graph, count, new_edge)

            temp = temp.next




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

converting_graph(graph,vertices)
print(max_degree(graph))


