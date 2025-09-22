def two_sum_revisited(arr1_len,arr2_len,arr_1,arr_2,sum):
    left = 0
    right = arr2_len-1
    diff = float("inf")
    temp = [left+1,right+1]
    while left < arr1_len and right >= 0:
        if(arr_1[left]+arr_2[right]==sum):
            print(left+1,right+1)
            return
        elif(arr_1[left]+arr_2[right]<sum):
            if(abs(arr_1[left]+arr_2[right]-sum)<diff):
                diff = abs(arr_1[left]+arr_2[right]-sum)
                temp[0] = left+1
                temp[1] = right+1
            left+=1

        else:
            if(abs(arr_1[left]+arr_2[right]-sum)<diff):
                diff = abs(arr_1[left]+arr_2[right]-sum)
                temp[0] = left+1
                temp[1] = right+1
            right-=1


    print(f"{temp[0]} {temp[1]}")


arr1_len, arr2_len, k = map(int,input().split(" "))
arr_1 = input().split(" ")
arr_2 = input().split(" ")
for i in range(arr1_len):
    arr_1[i] = int(arr_1[i])
for i in range(arr2_len):
    arr_2[i] = int(arr_2[i])

two_sum_revisited(arr1_len,arr2_len,arr_1,arr_2,k)
