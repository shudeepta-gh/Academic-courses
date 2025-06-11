result_dict = {}
inp = input()
lower_inp = ''
for char in inp:
  if char == ' ':
    continue
  elif ord('A') <= ord(char) <= ord('Z'):
    lower_inp += chr(ord(char) + 32)
  else:
    lower_inp += char

for char in lower_inp:
  if char in result_dict.keys():
    result_dict[char] += 1
  else:
    result_dict[char] = 1

print(result_dict)
