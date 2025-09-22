
def lower_bound(arr, low, high, value):
    if low >= high:
        return low
    mid = (low + high) // 2
    if arr[mid] < value:
        return lower_bound(arr, mid + 1, high, value)
    else:
        return lower_bound(arr, low, mid, value)

def upper_bound(arr, low, high, value):
    if low >= high:
        return low
    mid = (low + high) // 2
    if arr[mid] <= value:
        return upper_bound(arr, mid + 1, high, value)
    else:
        return upper_bound(arr, low, mid, value)


n,q = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
for i in range(q):
    x,y = map(int,input().split())
    left = lower_bound(arr, 0, n, x)
    right = upper_bound(arr, 0, n, y)
    print(right - left)
