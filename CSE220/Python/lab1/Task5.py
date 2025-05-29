class Node:
  def __init__(self,data):
    self.data=data
    self.next=None


def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode=Node(arr[i])
    tail.next=newNode
    tail=newNode

  return head

def sum_dist(head, arr):
  sum=0

  for i in arr:
    temp=head
    count=0

    while(temp!=None):

      if(count==i):
        sum+=temp.data
        break

      count+=1
      temp=temp.next

  return sum

print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()
