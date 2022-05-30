from zad11ktesty import runtests

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


runtests ( kontenerowiec )
    
