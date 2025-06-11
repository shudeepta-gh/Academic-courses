def sum_of_leaves(root, sum=0):
  if(root==None):
    return sum

  if(root.left==None and root.right==None):
    sum += root.elem


  sum = sum_of_leaves(root.left, sum)
  sum = sum_of_leaves(root.right, sum)

  return sum



#DRIVER CODE
root = BTNode(30)
root.left = BTNode(10)
root.left.left = BTNode(3)
root.left.left.left = BTNode(2)
root.left.right = BTNode(15)
root.right = BTNode(40)
root.right.left = BTNode(35)
root.right.left.right = BTNode(36)
root.right.right = BTNode(55)
inorder(root)
print()
print(sum_of_leaves(root, 0))
