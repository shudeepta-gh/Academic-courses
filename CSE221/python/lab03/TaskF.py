def Ordering_B_tree(low,high):
        if(low > high):
            return []
        mid = (low + high)//2
        left = Ordering_B_tree(low,mid - 1)
        right = Ordering_B_tree(mid + 1,high)
        return [A[mid]] + left + right


N = int(input())
A = list(map(int,input().split()))
order = Ordering_B_tree(0,N - 1)
print(' '.join(map(str,order)))
