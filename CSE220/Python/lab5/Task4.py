def task4A_recursive( head ):
    if(head==None):
      return

    task4A_recursive( head.next )
    print(head.elem,end=" ")

def task4B_recursive( head ):
    if(head.next==None):
      return head

    new_head = task4B_recursive(head.next)
    head.next.next=head
    head.next=None
    return new_head

arr = np.random.randint(1, 20, size=6, dtype=int)

print("task4A_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(arr[::-1])[1:-1] )
print( "Your Output    : ",end="" )
task4A_recursive( head )
print()

#--------------------------------------------------------

# task4B_recursive
print("\ntask4B_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",str(arr[::-1])[1:-1] )
print( "Your Output    : ",end="" )
head = task4B_recursive( head )
showLL(head)
print()
