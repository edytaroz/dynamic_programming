from zad11ktesty import runtests

def get_sum(T,sum):
    n = len(T)
    t = [[False for _ in range(n+1)] for _ in range(sum+1)]
    for i in range(n):
        if T[i] < sum + 1:
            t[T[i]][0] = True
    for i in range(1,n+1):
        for j in range(sum+1):
            if T[i] < ...:
                ...

def suma(T):
    n = len(T)
    sumaa = 0
    for i in range(n):
        sumaa += T[i]
    rem = 0
    flag = False
    for i in range(sumaa//2,-1,-1):
        if not flag:
            if get_sum(T,i):
                rem = i
                flag = True
    return (sumaa - rem*2)//2

def rek(T,i,sum1,sum2):
    if i >= len(T) - 1:
        return abs(sum1-sum2)
    else:
        return min(rek(T,i+1,sum1+T[i+1],sum2),rek(T,i+1,sum1,sum2+T[i+1]))

def dyn(T):
    n = len(T)
    print(T)
    sumy = sum(T)
    tab = [[0 for _ in range(sumy+1)] for _ in range(n+1)]
    tr = [[False for _ in range(sumy+1)] for _ in range(n+1)]
    for i in range(n+1):
        tr[i][0] = True
    tr[1][0] = True
    tr[1][T[0]] = True
    for i in range(1,n+1):
        for j in range(1,sumy+1):
            if tr[i-1][j] or tr[i-1][j-T[i-1]]:
                tr[i][j] = True
    mx = sumy
    for i in range(1,sumy+1):
        for j in range(1,n+1):
            if tr[j][i]:
                if mx > abs(sumy - 2*i):
                    mx = abs(sumy - 2*i)
    return mx


def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    return dyn(T)
    #return rek(T,-1,0,0)

runtests ( kontenerowiec )
    