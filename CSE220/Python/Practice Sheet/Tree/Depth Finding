def correct_depth(root,elem):
  if(root.elem == elem):
    return 0

  if(root == None):
    return -1

  left_depth = correct_depth(root.left, elem)
  if left_depth != -1:
        return 1 + left_depth

  right_depth = correct_depth(root.right, elem)
  if right_depth != -1:
        return 1 + right_depth

  return -1
