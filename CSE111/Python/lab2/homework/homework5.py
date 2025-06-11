def key_generator(*employees):
  list1=[]
  for employee in employees:
     key=""
     key+=employee[0].lower()
     for i in range(len(employee)-2,0,-1):
       key+=str(ord(employee[i]))
     key+=employee[-1].upper()
     list1.append(key)

  return list1

key_list=key_generator("Alex","Bob","Trudy")
print("Encrypted Keys:",key_list)
