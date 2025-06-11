def is_james_bond(integer_list):

  str_1=""
  for i in range(len(integer_list)):
    if integer_list[i]==0 or integer_list[i]==7:
      str_1+=str(integer_list[i])

  if len(str_1)>3:
    return False

  for i in range(2,len(str_1),1):
    if f"{str_1[i-2]}{str_1[i-1]}{str_1[i]}"=="007":
      return True
    else:
      return False



print(is_james_bond( [1, 2, 4, 0, 0, 7, 5] ))
print(is_james_bond( [1, 7, 2, 0, 4, 5, 0] ))
print(is_james_bond( [1, 0, 2, 0, 4, 7, 5] ))
