def remove_block(stack, n):
  temp_st = Stack()
  for i in range(n-1):
    temp_st.push(stack.pop())

  stack.pop()
  for i in range(n-1):
    stack.push(temp_st.pop())

  return stack


print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()
