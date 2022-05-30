from zad12ktesty import runtests 

def rek(P,T,i,k):
    if i == 0:
        return 0
    if k <= 0:
        return 0
    if k == 1:
        suma = 0
        for j in range(i):
            suma += T[j]
        return suma
    mini = float('inf')
    for j in range(i):
        suma = 0
        for p in range(j+1,i):
            suma += T[p]
        s = max(suma,rek(P,T,j,k-1))
        if s < mini:
            mini = s
    return mini

def fun(T,k):
    n = len(T)
    tab = [[0 for _ in range(n)] for _ in range(k)]
    if k <= 0:
        return 0
    if k == 1:
        suma = 0
        for i in range(n):
            suma += T[i]
        return suma
    tab[1][0] = T[0]
    for i in range(1,n):
        tab[1][i] = tab[1][i-1] + T[i]
    mini = float('inf')
    print(tab[1])
    for i in range(1,k):
        print(tab[i])
        for j in range(1,n):
            suma = 0
            for t in range(j,n):
                suma += T[t]
            tab[i][j] = max(suma,tab[i-1][j])
    if n < 100:
        for i in range(k):
            print(tab[i])
    for i in range(1,n-1):
        if tab[k-1][i] < mini:
            mini = tab[k-1][i]
    return mini

def autostrada( T, k ):
    print(T)
    #Tutaj proszę wpisać własną implementację
    P = [[0 for _ in range(len(T))]for _ in range(k+1)]
    #return rek(P,T,len(T),k)
    return fun(T,k)


runtests ( autostrada,all_tests=True )