N = int(input())
swap_count = 0
str_id = input()
str_marks = input()
id = str_id.split(" ")
marks = str_marks.split(" ")

for i in range(N-1):
    max_mark = i

    for j in range(i+1,N):
        if(int(marks[j])>int(marks[max_mark])):
            max_mark = j

        elif int(marks[j]) == int(marks[max_mark]) and int(id[j]) < int(id[max_mark]):
            max_mark = j

    if(max_mark!=i):
       marks[i],marks[max_mark] = marks[max_mark],marks[i]
       id[i],id[max_mark] = id[max_mark],id[i]
       swap_count+=1

print(f"Minimum swaps: {swap_count}")
for i in range(N):
    print(f"ID: {id[i]} Mark: {marks[i]}")
