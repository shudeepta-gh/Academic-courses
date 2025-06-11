word=input("Enter the word:")
new_word=[]
for i in range(len(word)):
  if word[i]!=" ":
    new_word.append(word[i])
count=0
for i in range(len(new_word)):
    if(new_word[i]==new_word[len(new_word)-i-1]):
      count+=1
if(count==len(new_word)):
  print("Palindrome")
else:
  print("Not a palindrome")
