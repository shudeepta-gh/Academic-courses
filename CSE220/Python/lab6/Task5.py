def leftsum(root):
  if(root==None):
    return 0

  return root.elem + leftsum(root.left) + leftsum(root.right)


def rightsum(root):
  if(root==None):
    return 0

  return root.elem + rightsum(root.left) + rightsum(root.right)


def subtract_summation(root):

   if(root==None):
     return 0

   return leftsum(root.left)-rightsum(root.right)




#Driver Code
root=BTNode(71)
node1 = BTNode(27)
node2 = BTNode(62)
node3 = BTNode(80)
node4 = BTNode(75)
node5 = BTNode(87)
node6 = BTNode(56)
node7 = BTNode(41)
node8 = BTNode(3)
node9 = BTNode(19)
node10 = BTNode(89)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node3.left = node5
node3.right = node6
node2.left = node7
node2.right = node8
node8.left = node9
node8.right = node10


print(subtract_summation(root)) #This should print 111
