def beautiful_list(n,m,list1,list2):

    left = right = 0
    final_list = []
    while(left<n and right<m):
        if(list1[left]<list2[right]):
            final_list.append(list1[left])
            left+=1

        elif(list1[left]>list2[right]):
            final_list.append(list2[right])
            right+=1

        else:
            final_list.append(list1[left])
            final_list.append(list2[right])
            left+=1
            right+=1
    final_list.extend(list1[left:])
    final_list.extend(list2[right:])
    final_list = list(map(str,final_list))
    print(" ".join(final_list))



N = int(input())
list1 = list(map(int,input().split(" ")))
M = int(input())
list2 = list(map(int,input().split(" ")))

beautiful_list(N,M,list1,list2)
