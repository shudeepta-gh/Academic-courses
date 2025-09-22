def two_pointer_sort(len,target_sum,arr):

   left = 0
   right = len-1
   while(left<right):
       if(arr[left]+arr[right]==target_sum):
           print(f"{left+1} {right+1}")
           return

       elif(arr[left]+arr[right]>target_sum):

           right-=1

       else:
           left+=1

   print(-1)


len,target_sum = input().split(" ")
len = int(len)
target_sum = int(target_sum)
arr = input().split(" ")
for i in range(len):
    arr[i] = int(arr[i])

two_pointer_sort(len,target_sum,arr)
