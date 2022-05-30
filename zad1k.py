from zad1ktesty import runtests

def fun(S):
    n = len(S)
    tab1 = [0 for _ in range(n)]
    tab0 = [0 for _ in range(n)]
    tab = [0 for _ in range(n)]
    if S[0] == '1':
        tab1[0] = 1
    else:
        tab0[0] = 1
    for i in range(1,n):
        if S[i] == '0':
            tab0[i] = tab0[i-1] + 1
            tab1[i] = tab1[i-1]
        else:
            tab1[i] = tab1[i-1] + 1
            tab0[i] = tab0[i-1]
    if tab1[n-1] == n :
        return -1
    tab[0] = tab0[0] - tab1[0]
    for i in range(1,n):
        maks = tab0[i] - tab1[i]
        for j in range(i):
            if tab0[i] - tab0[j] - tab1[i] + tab1[j] > maks:
                maks = tab0[i] - tab0[j] - tab1[i] + tab1[j]
        for j in range(i):
            if tab[j] > maks:
                maks = tab[j]
        tab[i] = maks
    return tab[n-1]



def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    return fun(S)

runtests ( roznica )