from zad4ktesty import runtests

def iter(T):
    n = len(T)
    tab = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        tab[0][i] = tab[0][i-1] + T[0][i]
        tab[i][0] = tab[i-1][0] + T[i][0]
    for i in range(1,n):
        for j in range(1,n):
            tab[i][j] = min(tab[i-1][j],tab[i][j-1])
            tab[i][j] += T[i][j]
    return tab[n-1][n-1]

def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    return iter(T)

runtests ( falisz )
