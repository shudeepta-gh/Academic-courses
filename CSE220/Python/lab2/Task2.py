def NodeAt(head,idx):
  temp = head
  count = 0
  while(temp != None):
    if(count==idx):
      return temp.elem
    count += 1
    temp = temp.next

def length(head):
  temp = head
  count = 0
  while(temp != None):
    count += 1
    temp = temp.next

  return count

def reverse(head):
   prev = None
   temp = head
   while (temp != None):
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node


   return prev


def word_Decoder(head):
  position=13 % length(head)

  if(position<length(head)):
    newhead=Node(NodeAt(head,position))
    tail=newhead
    for i in range(position+position,length(head),position):

         data = NodeAt(head,i)
         newNode = Node(data)
         tail.next = newNode
         tail = newNode

    dummy = Node(None)
    tail.next = dummy
    tail = dummy
    return reverse(newhead)


print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N
