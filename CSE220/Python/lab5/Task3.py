class Node:
  def __init__(self, value=None, next = None):
    self.elem = value
    self.next = next

def showLL(head):
  if head!=None:
    n = head
    while n!=None:
        print(n.elem, end=' -> ')
        n = n.next
    print()

def arr2LL(arr):
  head = Node(arr[0])
  n = head
  for i in range(1,len(arr)):
      newNode = Node(arr[i])
      n.next = newNode
      n = newNode
  tail = n
  return head

def task3A( head ):
  temp=head
  while(temp!=None):
    print(temp.elem,end=" ")
    temp=temp.next


def task3B_recursive( head ):
    if(head==None):
      return
    print(head.elem,end=" ")
    task3B_recursive( head.next )


def task3C( head ):
   temp=head
   sum=0
   while(temp!=None):
     sum+=temp.elem
     temp=temp.next
   return sum


def task3D_recursive( head ):
    if(head==None):
      return 0

    return head.elem + task3D_recursive(head.next)

def task3E( head ):
   temp=head
   sum=0
   mul=1
   while(temp!=None):
     if(temp.elem%2==0):
       mul*=temp.elem
     else:
       sum+=temp.elem
     temp=temp.next
   return sum-mul

def task3F_recursive( head , oddSum=0 , evenMul=1 ):
    if(head!=None):
      if(head.elem%2==0):
        evenMul*=head.elem
      else:
        oddSum+=head.elem

      return task3F_recursive( head.next , oddSum , evenMul )

    else:
      return oddSum-evenMul

arr = np.random.randint(1, 20, size=6, dtype=int)

# task3A
print("task3A: ")
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3A( head )
print()

# task3B_recursive
print("\ntask3B_recursive: ")
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3B_recursive( head )
print()

#--------------------------------------------------------

arr = np.random.randint(1, 10, size=6, dtype=int)

# task3C
print("\ntask3C: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3C( head ) )

# task3D_recursive
print("\ntask3D_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3D_recursive( head ) )

#--------------------------------------------------------

arr = np.random.randint(1, 8, size=5, dtype=int)

# task3E
print("\ntask3E: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.sum([e for e in arr if e%2!=0])-np.prod([e for e in arr if e%2==0]) )
print( "Your Output    : ",task3E( head ) )

#--------------------------------------------------------

# task3F
print("\ntask3F_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.sum([e for e in arr if e%2!=0])-np.prod([e for e in arr if e%2==0]) )
print( "Your Output    : ",task3F_recursive( head ) )
