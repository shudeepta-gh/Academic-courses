def conditional_reverse(stack):

  temp_st = Stack()
  while(stack.peek()!=None):
    if(temp_st.peek()!=stack.peek()):
       temp_st.push(stack.pop())
    else:
      stack.pop()

  return temp_st


print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
if reversed_stack==None:
    print("Incomplete Task")
else:
    print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')
