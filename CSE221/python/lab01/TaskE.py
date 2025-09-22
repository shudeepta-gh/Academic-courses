def increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
if increasing(arr):
    print("Yes")
else:
    if n == 1:
        print("YES")
    elif n == 2:
        if arr[0] <= arr[1]:
            print("YES")
        else:
            print("NO")
    else:
        even = arr[1::2]
        odd = arr[::2]
        even_sorted = sorted(even)
        odd_sorted = sorted(odd)

        merged = []
        o_ptr = e_ptr = 0
        for i in range(n):
            if i % 2 == 0:
                if o_ptr < len(odd_sorted):
                    merged.append(odd_sorted[o_ptr])
                    o_ptr += 1
            else:
                if e_ptr < len(even_sorted):
                    merged.append(even_sorted[e_ptr])
                    e_ptr += 1

        if increasing(merged):
            print("YES")
        else:
            print("NO")
