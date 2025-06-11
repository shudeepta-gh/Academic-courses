string1=input("Enter a string seperated by space:")
string2=input("Enter a string seperated by space:")
list1=string1.split()
for ind in range(len(list1)):
  list1[ind]=int(list1[ind])
list2=string2.split()
for ind in range(len(list2)):
  list2[ind]=int(list2[ind])
list3=[]
for i in range(len(list1)):
  for j in range(len(list2)):
    multiplication=list1[i]*list2[j]
    list3.append(multiplication)
print(list3)
