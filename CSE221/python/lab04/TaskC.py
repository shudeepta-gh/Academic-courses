def adj_listTomatrix(matrix,i,k):
    for j in range(k[0]):

        matrix[i][k[j+1]] = 1

n = int(input())
matrix = [[0]*n for i in range(n)]
for i in range(n):
    k = list(map(int, input().split(' ')))
    adj_listTomatrix(matrix,i,k)


for i in range(len(matrix)):
    print(' '.join(map(str, matrix[i])))
