def longest_K_distinct(arr,n,k):
    count_dict = {}
    max_len = 0
    left = right = 0
    while(right<n):
        if(arr[right] not in count_dict):
            count_dict[arr[right]] = 1
        else:
            count_dict[arr[right]] +=1


        while(left<=right and len(count_dict)>k):
            count_dict[arr[left]] -= 1
            if(count_dict[arr[left]]==0):
                del(count_dict[arr[left]])
            left+=1

        current_len = right - left + 1
        if(current_len>max_len):
            max_len = current_len
        right+=1


    return max_len

n,k = map(int,input().split(" "))
arr = list(map(int,input().split()))
result = longest_K_distinct(arr,n,k)
print(result)
