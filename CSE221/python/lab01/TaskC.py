T = int(input())

for i in range(T):
    length = int(input())
    str_arr = input()
    arr = str_arr.split(" ")
    is_incre = True
    for i in range(length-1):
        if(int(arr[i]) > int(arr[i+1])):
            is_incre = False

    if(is_incre==True):
        print("YES")
    else:
        print("NO")
