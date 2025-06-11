def sort(input_list):
  result_str = ''
  for i in range(len(input_list)-1):
    min_idx = i
    for j in range(i+1,len(input_list)):
      if input_list[j] < input_list[min_idx]:
        min_idx = j

    temp = input_list[i]
    input_list[i] = input_list[min_idx]
    input_list[min_idx] = temp

  for num in input_list:
    result_str += chr(num)

  return result_str
inp = input("Enter your string:")
low_case = []
up_case = []
odd_digits = []
even_digits = []
for i in range(len(inp)):
  if ord('A') <= ord(inp[i]) <= ord('Z'):
    up_case.append(ord(inp[i]))
  elif ord('a') <= ord(inp[i]) <= ord('z'):
    low_case.append(ord(inp[i]))
  elif int(inp[i]) % 2 == 0:
    even_digits.append(ord(inp[i]))
  else:
    odd_digits.append(ord(inp[i]))

result = sort(low_case) + sort(up_case) + sort(odd_digits) + sort(even_digits)

print(result)
