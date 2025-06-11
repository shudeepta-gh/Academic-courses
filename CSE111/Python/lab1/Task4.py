while True:
  result = 'UB Jumper'
  inp = input('Input the list: ')#"1 4 2 3"
  if inp == 'STOP':
    break
  inp = inp.split()#["1","4","2","3"]
  for i in range(len(inp)):
    inp[i] = int(inp[i])#[1,4,2,3]

  req_diffs = []
  for i in range(1,len(inp)):#[1,2,3]
    req_diffs.append(i)

  diffs_list = []
  for i in range(len(inp) - 1):
    diff = inp[i] - inp[i + 1]
    if diff < 0:
      diff = -1*diff
    diffs_list.append(diff)

  for num in req_diffs:
    if num not in diffs_list:
      result = 'Not UB Jumper'
      break
  print(result)
