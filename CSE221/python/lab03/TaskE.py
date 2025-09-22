def fast_pow(a,b,mod):
    result = 1
    a = a % mod
    while(b>0):
        if(b%2 == 1):
            result = (result*a) % mod
        a = (a*a) % mod
        b = b//2
    return result

def series_drift():
    T = int(input())
    for test in range(T):
        a,n,m = map(int, input().split())
        if(a == 1):
            print(n % m)
        else:
            mod = m*(a - 1)
            a_pow_n = fast_pow(a,n,mod)
            num = (a*(a_pow_n-1)) % mod
            sum = num//(a-1)
            print(sum % m)


series_drift()
