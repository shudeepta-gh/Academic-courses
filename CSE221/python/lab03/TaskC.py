
def fast_power_drift(a,b,m):


    result = 1
    a = a % m
    while(b>0):
        if(b % 2 != 0):
            result = (result*a) % m
        a = (a**2) % m
        b = b//2

    return result


a,b = map(int,input().split(" "))
print(fast_power_drift(a,b,107))
