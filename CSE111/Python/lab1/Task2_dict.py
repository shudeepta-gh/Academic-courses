result_dict = {}
while True:
  inp = input()
  if inp == 'STOP':
    break

  if int(inp) in result_dict.keys():
    result_dict[int(inp)] += 1
  else:
    result_dict[int(inp)] = 1

for k,v in result_dict.items():
  print(f'{k} - {v} times')
