list1=[]

N=int(input("Enter a number:"))
for i in range(0,N,1):
  num=input("Enter a string seperated by space:")
  m=num.split()
  for ind in range(len(m)):
    m[ind]=int(m[ind])
  list1.append(m)  #[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]

max=0
maxlist=[]#[[1,2,3]]
for i in list1:
  sum=0
  for j in i:
    sum+=int(j)
  if sum>max:
    max=sum
    maxlist=i
print(max)
print(maxlist)
