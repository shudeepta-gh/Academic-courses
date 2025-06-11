list1=[]
list2=[]
list3=[]
while True:
  num=input("Enter a number:")
  if num=="STOP":
    break
  else:
    list1.append(int(num))
    if int(num) not in list2:
      list2.append(int(num))

for i in range(len(list2)):
  counter=0
  for j in range(len(list1)):
    if list2[i]==list1[j]:
     counter+=1
  list3.append(counter)

for i in range(len(list2)):
  print(list2[i],"-",list3[i],"times")
