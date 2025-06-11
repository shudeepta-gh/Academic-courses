def LCA(root, x, y):

  if(root==None):
    return None

  if(root.elem==x or root.elem==y):
    return root.elem

  if(x>root.elem and y>root.elem):
    return LCA(root.right,x,y)

  if(x<root.elem and y<root.elem):
    return LCA(root.left,x,y)


  return root.elem


#DRIVER CODE
root = BTNode(15)
root.left = BTNode(10)
root.left.left = BTNode(8)
root.left.left.left = BTNode(6)
root.left.left.right = BTNode(9)
root.left.right = BTNode(12)
root.right = BTNode(25)
root.right.right = BTNode(30)
root.right.left = BTNode(20)
root.right.left.left = BTNode(18)
root.right.left.right = BTNode(22)


inorder(root)
print()
print(LCA(root, 12, 6))

print(LCA(root, 20, 6))

print(LCA(root, 18, 22))
print(LCA(root, 20, 25))
