N = int(input())
input_str = input()
arr = input_str.split()



while True:
    swapped = False
    for i in range(N-1):
        if int(arr[i]) > int(arr[i+1]):
            if int(arr[i])%2 == 0 and int(arr[i+1])%2 == 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            elif int(arr[i])%2 != 0 and int(arr[i+1])%2 != 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    if(swapped==False):
        break

print(" ".join(arr))
