
def find_index(arr,target):
    for i in range(len(arr)):
        if (arr[i]==target):
            return i
    return -1

def post_traversal(in_order,pre_order):
    if not pre_order:
        return []

    root = pre_order[0]
    root_idx = find_index(in_order, root)
    left_in = in_order[:root_idx]
    right_in = in_order[root_idx+1:]

    left_pre = pre_order[1:1+len(left_in)]
    right_pre = pre_order[1+len(left_in):]

    left_post = post_traversal(left_in,left_pre)
    right_post = post_traversal(right_in,right_pre)

    return left_post + right_post + [root]

N = int(input())
in_order = list(map(int,input().split()))
pre_order = list(map(int,input().split()))
post_order = post_traversal(in_order,pre_order)
print(' '.join(map(str,post_order)))
