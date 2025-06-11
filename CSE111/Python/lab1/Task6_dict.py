numpad_dict = {1: '.,?!:', 2:'ABC', 3: 'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS',8:'TUV', 9:'WXYZ', 0:' '}
output = ''
inp_1 = input()
str_1 = ''
for char in inp_1:
  if ord('a') <= ord(char) <= ord('z'):
    str_1 += chr(ord(char) - 32)
  else:
    str_1 += char

for char in str_1:
  for k,v in numpad_dict.items():
    if char in v:
      idx = None
      #linear search for the character inside the value
      for i in range(len(v)):
        if v[i] == char:
          idx = i
      output += str(k) * (idx + 1)

print(output)
