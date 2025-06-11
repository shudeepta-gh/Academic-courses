
inp_1 = input().split()
for i in range(len(inp_1)):
  inp_1[i] = int(inp_1[i])
n = inp_1[0]
k = inp_1[1]

inp_2 = input().split()
for i in range(len(inp_2)):
  inp_2[i] = int(inp_2[i])

allowed_students = 0
for i in range(len(inp_2)):
  if inp_2[i] + k <= 5:
    allowed_students += 1

print(allowed_students // 3)
