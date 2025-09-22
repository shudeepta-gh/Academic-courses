
T = int(input())

for i in range(T):
    ar_exp = input()
    temp = ar_exp.split(" ")
    a = int(temp[1])
    b = int(temp[3])
    op = temp[2]


    if(op=="+"):
        result = a+b
    elif(op=="-"):
        result = a-b
    elif(op=="*"):
        result = a*b
    elif(op=="/"):
        result = a/b
    print(f"{result:.6f}")
