n = int(input())
for i in range(n):
    k,x = map(int,input().split())
    result = k+(k-1)//(x-1)
    print(result)
