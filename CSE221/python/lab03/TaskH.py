
def find_index(arr,target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1

def pre_Traversal(in_order,post_order):
    if not post_order:
        return []
    root = post_order[-1]
    root_idx = find_index(in_order,root)
    left_in = in_order[:root_idx]
    right_in = in_order[root_idx+1:]
    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in):-1]
    left_pre = pre_Traversal(left_in,left_post)
    right_pre = pre_Traversal(right_in,right_post)
    return [root] + left_pre + right_pre

N = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
pre_order = pre_Traversal(in_order,post_order)
print(' '.join(map(str,pre_order)))
