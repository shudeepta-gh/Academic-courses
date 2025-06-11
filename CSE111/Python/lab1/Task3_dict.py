dict_1 = {}
inp_1 = input()
pair_list_1 = inp_1.split(', ')

for pair in pair_list_1:
  kv = pair.split(' : ')
  dict_1[kv[0]] = (kv[1])

result_dict = {}


for k,v in dict_1.items():
  if v in result_dict.keys():
    result_dict[v].append(k)
  else:
    result_dict[v] = [k]

print(result_dict)
