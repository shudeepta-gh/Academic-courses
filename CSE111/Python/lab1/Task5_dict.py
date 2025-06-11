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
