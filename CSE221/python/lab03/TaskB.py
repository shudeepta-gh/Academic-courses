
import math
import bisect
def count_inversion(arr):
    final_arr , count = divide_and_count(0,len(arr)-1,arr)
    return count

def divide_and_count(low,high,arr):

    if(low==high):
        return [arr[low]],0

    mid = (low+high)//2
    left,left_count = divide_and_count(low,mid,arr)
    right,right_count = divide_and_count(mid+1,high,arr)
    merge,merge_count = comparing_pairs(left,right)

    return merge,left_count+right_count+merge_count

def comparing_pairs(left,right):
    count = 0
    abs_right = []
    for i in range(len(right)):
        abs_right.append(abs(right[i]))

    abs_sorted_right = sorted(abs_right)

    for i in left:
        if(i>0):
            root = math.sqrt(i)
            count+=bisect.bisect_left(abs_sorted_right,root)

    i=j=0
    final=[]

    while(i<len(left) and j<len(right)):
        if(abs(left[i])<=abs(right[j])):
            final.append(left[i])
            i+=1

        else:
            final.append(right[j])
            j+=1

    final.extend(left[i:])
    final.extend(right[j:])
    return final,count



n = int(input())
arr = list(map(int, input().split()))
print(count_inversion(arr))
