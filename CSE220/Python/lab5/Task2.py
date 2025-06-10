def task2A( arr ):
    count=0
    while(count<arr.size):
      print(arr[count],end=" ")
      count+=1

def task2B_recursive( arr , idx):
    if(idx==arr.size):
      return
    print(arr[idx],end=" ")
    task2B_recursive( arr , idx+1)


def task2C( arr ):
    count = 0
    sum=0
    while(count<arr.size):
     sum+=arr[count]
     count+=1
    return sum


def task2D_recursive( arr ,idx=0):
    if(idx==arr.size):
      return 0
    return arr[idx] + task2D_recursive( arr ,idx+1)

def task2E( arr ):
    count=0
    sum=0
    mul=1
    while(count<arr.size):
      if(arr[count]%2==0):
        sum+=arr[count]
        count+=1

      else:
        mul*=arr[count]
        count+=1

    return mul-sum


def task2F_recursive( arr, i=0, oddProduct=1, sumEven=0 ):
    if(i >= 0 and i < len(arr)):
      if(arr[i] % 2 == 0):
        sumEven += arr[i]
      else:
        oddProduct *= arr[i]
      return task2F_recursive(arr, i+1, oddProduct, sumEven)
    return oddProduct - sumEven

print("Task2A: ")
arr = np.random.randint(1, 20, size=6, dtype=int)
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2A( arr )
print()

# task2B_recursive
print("\nTask2B_recursive: ")
arr = np.random.randint(1, 20, size=6, dtype=int)
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2B_recursive(arr,0)
print()

# task2C
print("\nTask2C: ")
arr = np.random.randint(1, 10, size=6, dtype=int)
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2C(arr) )

# task2D_recursive
print("\nTask2D_recursive: ")
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2D_recursive( arr ) )

# task2E
print("\nTask2E: ")
arr = np.random.randint(1, 8, size=5, dtype=int)
print("The Array: ",arr)
print( "Expected Output: ",np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0]) )
print( "Your Output    : ",task2E( arr ) )


# task2F
print("\nTask2F_recursive: ")
print("The Array: ",arr)
print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task2F_recursive( arr ))
