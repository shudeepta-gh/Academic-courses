def find_Path(root, key, root_list=None):

    if (root_list==None):
        root_list = []

    if (root==None):
       return "No path found"

    root_list.append(root.elem)

    if(root.elem == key):
        return root_list

    if(key < root.elem):
        return find_Path(root.left, key, root_list)
    elif(key > root.elem):
        return find_Path(root.right, key, root_list)



#DRIVER CODE
root = BTNode(30)
root.left = BTNode(10)
root.right = BTNode(40)
root.left.left = BTNode(3)
root.left.right = BTNode(15)
root.right.left = BTNode(35)
root.right.right = BTNode(55)

inorder(root)
print()
print(find_Path(root,15))
#This should print [30,10,15]

print(find_Path(root,50))
#This should print No Path Found
