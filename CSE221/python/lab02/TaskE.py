def longest_sub_sum(arr,n,k):
    left = 0
    right = 0

    sum = 0
    max_len = 0

    while(right<n):
        sum+=arr[right]

        while(left<=right and sum>k):
            sum -= arr[left]
            left+=1


        len = right-left+1
        if(len>max_len):
             max_len = len

        right+=1

    return max_len

n,k = map(int,input().split(" "))
arr = list(map(int,input().split()))
result = longest_sub_sum(arr,n,k)
print(result)
