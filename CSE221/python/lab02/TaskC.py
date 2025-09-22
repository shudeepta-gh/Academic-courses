
def merge_sort(arr,low,high):
    mid = (low+high)//2
    if(low == high):
        return [arr[low]]
    elif(low<high):
       left = merge_sort(arr,low,mid)
       right = merge_sort(arr,mid+1,high)
       return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while(i<len(left) and j<len(right)):
        if(left[i][1]<=right[j][1]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def triple_the_trouble(n,arr,sum):
    for i in range(n):
        left = i+1
        right = n-1
        while(left<right):
            if(arr[left][1]+arr[right][1]==sum-arr[i][1]):
                print(f"{arr[i][0]} {arr[left][0]} {arr[right][0]}")
                return


            elif(arr[left][1]+arr[right][1]<sum-arr[i][1]):
                left+=1

            else:
                right-=1

    print(-1)


n,tar_sum = map(int,input().split(" "))
arr = input().split(" ")

for i in range(n):
    k_v = [0,0]
    k_v[0] = i+1
    k_v[1] = int(arr[i])
    arr[i] = k_v

res_arr = merge_sort(arr,0,n-1)

triple_the_trouble(n,res_arr,tar_sum)
