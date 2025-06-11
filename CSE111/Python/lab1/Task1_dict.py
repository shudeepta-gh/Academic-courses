d1 = {'a': 100, 'b': 100, 'c': 200, 'd': 300}
d2 = {'a': 300, 'b': 200, 'd': 400, 'e': 200}

for k, v in d2.items():
    if k not in d1.keys():
        d1[k] = v
    else:
        d1[k] = d1[k] + v

print(d1)

result_list= []
for k,v in d1.items():
  if v not in result_list:
    result_list.append(v)

for i in range(len(result_list)-1):
    min_idx = i
    for j in range(i+1, len(result_list)):
      if result_list[j] < result_list[min_idx]:
        min_idx = j

    temp = result_list[i]
    result_list[i] = result_list[min_idx]
    result_list[min_idx] = temp

result_tuple = tuple(result_list)
print("values:",result_tuple)
