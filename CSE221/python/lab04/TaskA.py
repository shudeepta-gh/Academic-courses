
def matrix_representation(matrix,start,end,weight):
    matrix[start-1][end-1] = weight

N,M = map(int,input().split(" "))
matrix = [[0]*N for i in range(N)]

for i in range(M):
    start,end,weight = map(int,input().split(" "))
    matrix_representation(matrix,start,end,weight)

for i in range(len(matrix)):
    print(' '.join(map(str, matrix[i])))
