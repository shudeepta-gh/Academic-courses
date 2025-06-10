def helper_sum(root,level=0):
  if(root==None):
    return 0


  if level==0:
    return root.elem + helper_sum(root.left,level+1) + helper_sum(root.right,level+1)

  else:
    return root.elem%level + helper_sum(root.left,level+1) + helper_sum(root.right,level+1)



def sumTree(root):
  return helper_sum(root)

root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15
