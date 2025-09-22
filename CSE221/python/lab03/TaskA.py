def merge(a,b):

    i = j = 0
    final = []
    count = 0

    while(i<len(a) and j<len(b)):
       if(a[i]<b[j]):
           final.append(a[i])
           i+=1

       elif(b[j]<a[i]):
           final.append(b[j])
           count += len(a)-i
           j+=1

       else:
           final.append(a[i])
           final.append(b[j])
           i+=1
           j+=1

    final.extend(a[i:])
    final.extend(b[j:])
    return final , count


def mergeSort(low,high,arr):

    if low==high:
        return [arr[low]],0

    else:
        mid = (low+high)//2
        a,a_count = mergeSort(low,mid,arr)
        b,b_count= mergeSort(mid+1,high,arr)
        merged,m_count = merge(a,b)

    return merged , a_count + b_count + m_count



n = int(input())
arr = list(map(int,input().split()))

result,inv_count= mergeSort(0,n-1,arr)

print(inv_count)
for i in result:
    print(i,end=" ")
