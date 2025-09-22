
def mat_multi(a,b,mod):
    res = [[0,0],[0,0]]
    res[0][0] = ((a[0][0]*b[0][0])+(a[0][1]*b[1][0]))%mod
    res[0][1] = ((a[0][0]*b[0][1])+(a[0][1]*b[1][1]))%mod
    res[1][0] = ((a[1][0]*b[0][0])+(a[1][1]*b[1][0]))%mod
    res[1][1] = ((a[1][0]*b[0][1])+(a[1][1]*b[1][1]))%mod

    return res

def fast_matrix_drift(mat,power,mod):
    result = [[1,0],[0,1]]
    while(power>0):
        if(power%2==1):
            result = mat_multi(result,mat,mod)
        mat = mat_multi(mat,mat,mod)
        power = power//2

    return result

mod = 10**9+7

T = int(input())
for i in range(T):
    a11,a12,a21,a22 = map(int,input().split())
    matrix = [[a11,a12],[a21,a22]]
    power = int(input())
    result = fast_matrix_drift(matrix,power,mod)
    print(result[0][0],result[0][1])
    print(result[1][0],result[1][1])
