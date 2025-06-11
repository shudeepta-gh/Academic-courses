string_1 = input("Enter the sentence:")
list_1=[]
for i in range(len(string_1)):
  list_1.append(string_1[i])

corrected_sentence=""
for i in range(len(list_1)):
  if list_1[i]=="i" and list_1[i+1]==" ":
    corrected_sentence+="I"


  elif i==0:
    if "a"<=list_1[i]<="z":
      corrected_sentence+=chr(ord(list_1[i])-32)

  elif list_1[i]=="." or list_1[i]=="?" or list_1[i]=="!":
    corrected_sentence+=list_1[i]
    if i!=len(list_1)-1:

      if "a"<=list_1[i+1]<="z":
         list_1[i+1]=chr(ord(list_1[i+1])-32)

  else:
    corrected_sentence+=list_1[i]

print(corrected_sentence)
