def add_up(head,elem):
  temp = head
  while(temp.next!=None):
    temp = temp.next

  temp.next = Node(elem)


def idGenerator(head1, head2, head3):

  newhead = reverse(head1)

  temp2 = head2
  temp3 = head3
  while(temp2 != None):
    sum = temp2.elem+temp3.elem
    if(sum<10):
      add_up(head1,sum)

    else:
      sum=  sum%10
      add_up(head1,sum)


    temp2 = temp2.next
    temp3 = temp3.next


  return newhead

print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
