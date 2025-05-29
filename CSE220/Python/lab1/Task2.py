def mostWater(arr):

  maximum_area=-1
  for i in range(arr.size):
    x=(i,0)
    y=(i,arr[i])
    w=arr[i]-i
    h=arr[arr[i]]
    area=w*h
    if(area>maximum_area):
      maximum_area=area

  return maximum_area


height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)
