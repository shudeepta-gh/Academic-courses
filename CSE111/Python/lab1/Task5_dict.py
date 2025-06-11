inp_1 = input('input 1: ')
str_1 = ''
for char in inp_1:
  if char == ' ':
    continue
  elif ord('A') <= ord(char) <= ord('Z'):
    str_1 += chr(ord(char) + 32)
  else:
    str_1 += char

inp_2 = input('input 1: ')
str_2 = ''
for char in inp_2:
  if char == ' ':
    continue
  elif ord('A') <= ord(char) <= ord('Z'):
    str_2 += chr(ord(char) + 32)
  else:
    str_2 += char
freq_dict_1 = {}
freq_dict_2 = {}

for char in str_1:
  if char in freq_dict_1.keys():
    freq_dict_1[char] += 1
  else:
    freq_dict_1[char] = 1

for char in str_2:
  if char in freq_dict_2.keys():
    freq_dict_2[char] += 1
  else:
    freq_dict_2[char] = 1

if freq_dict_1 == freq_dict_2:
  print('Those are anagrams')
else:
  print('Those are not anagrams')

#without using dict
word_1=input()
word_2=input()

count=0
str_1=' '
for char in word_1:
  if char == ' ':
    continue
  elif ord('A') <= ord(char) <= ord('Z'):
    str_1 += chr(ord(char) + 32)
  else:
    str_1 += char


str_2 = ''
for char in word_2:
  if char == ' ':
    continue
  elif ord('A') <= ord(char) <= ord('Z'):
    str_2 += chr(ord(char) + 32)
  else:
    str_2 += char


for i in range(len(str_1)):
  for j in range(len(str_2)):
    if(str_1[i]==str_2[j]):
       count+=1

if(count==len(word_1)):
  print("anagrams")
else:
  print("not anagrams")

