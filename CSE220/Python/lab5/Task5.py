import math
def findMax_recursive( head ):
    if(head.next==None):
      return -99999

    max = findMax_recursive( head.next )
    if(head.elem>max):
      max = head.elem
    return max


def sortLL_recursive( head ):
  if(head.next==None or head==None):
    return head

  min_node = head
  current_node=head.next
  while(current_node!=None):
    if(current_node.elem<min_node.elem):
      min_node = current_node
    current_node = current_node.next

  if(min_node!=head):
    temp = head.elem
    head.elem = min_node.elem
    min_node.elem =temp


  head.next = sortLL_recursive( head.next)

  return head


def findDup( head,index=0,record=[] ):
   if(head==None):
     return

   temp=head.next
   count = index+1
   idx_list = []
   for node in range(len(record)):
     if(record[node].elem==head.elem):
        idx_list.append(str(node))


   while(temp!=None):


     if(head.elem==temp.elem):
        idx_list.append(str(count))


     count+=1
     temp=temp.next
   if(len(idx_list)==0):
      print(head.elem,": No Duplicate")
   else:
      print(head.elem,":",", ".join(idx_list))

   if(head!=None):
     record.append(head)


   findDup( head.next,index+1,record)

arr = np.random.randint(1, 20, size=6, dtype=int)

# task5A
print("findMax_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",np.max(arr) )
print( "Your Output    : ",findMax_recursive(head) )

#--------------------------------------------------------

# task5B
print("\nsortLL_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(np.sort(arr))[1:-1] )
print( "Your Output    : ",end="" )
head = sortLL_recursive( head )
showLL(head)
print()

#--------------------------------------------------------

# task5C
print("\nfindDup: ")
print("The LinkedList: ",end="")
arr = np.array([10, 22, 13, 20, 22, 23, 10, 22])
head = arr2LL( arr )
showLL(head)
print( "\nExpected Output: " )
print("10: 6\n22: 4, 7\n13: No Duplicate\n20: No Duplicate\n22: 1, 7\n23: No Duplicate\n10: 0\n22: 1, 4\n")
print( "Your Output    : ",end="\n" )
findDup( head )
print()

