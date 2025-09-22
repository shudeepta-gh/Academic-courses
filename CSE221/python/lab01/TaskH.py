
N = int(input())
names = []
d_times = []
des = []
all_details = []
original_idx = []
for i in range(N):
    train = input()
    details = train.split(" ")
    names.append(details[0])
    des.append(details[4])
    hour,mins = details[-1].split(":")
    time = int(hour)*60 + int(mins)

    d_times.append(time)
    original_idx.append(i)
    all_details.append(train)


for i in range(N-1):
    min = i
    for j in range(i+1,N):
        if(names[j] < names[min]):
            min = j

        elif(names[j]==names[min]):
            if(d_times[j]>d_times[min]):
                min=j

            elif(d_times[j]==d_times[min]):
                if original_idx[j] < original_idx[min]:
                    min=j



    names[i], names[min] = names[min], names[i]
    d_times[i], d_times[min] = d_times[min], d_times[i]
    original_idx[i], original_idx[min] = original_idx[min], original_idx[i]
    all_details[i], all_details[min] = all_details[min], all_details[i]



for i in all_details:
    print(i)
