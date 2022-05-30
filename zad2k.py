from zad2ktesty import runtests

def is_palindrom(S,i,j):
    k = j + 1
    for a in range(i,j-(j-i)//2):
        k -= 1
        if S[a] != S[k]:
            return False
    return True

def palindrom1( S ):
    n = len(S)
    tab = [0 for _ in range(n)]#gdzie kończy się palindrom
    rem = ["" for _ in range(n)]#najdłuższy palindrom
    tab[0] = 0
    rem[0] = S[0]
    maks = 1
    if S[0] == S[1]:
        maks = 2
        tab[1] = 1
        rem[1] = rem[0]+S[1]
    else:
        tab[1] = 1
        rem[1] = S[1]
    for i in range(2,n):
        if tab[i-1] == i-1:
            if is_palindrom(S,i-len(rem[i-1])+1,i):
                ...
            else:
                ...
        elif tab[i-1] == i - 2:
            if is_palindrom(S,i-len(rem[i-1])+1,i):
                ...
            elif is_palindrom(S,i-len(rem[i-1])+1,i-1):
                ...
            else:
                ...
    return ""

def fun(S):
    n = len(S)
    tab = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tab[i][i] = True
    for i in range(1,n):
        for j in range(i):
            if i - j + 1 == 2:
                if S[i] == S[j]:
                    tab[j][i] = True
            elif S[j] == S[i] and tab[j+1][i-1]:
                tab[j][i] = True
            else:
                tab[j][i] = False
    maks = 0
    rem =[0,0]
    for i in range(n):
        for j in range(i):
            if tab[j][i]:
                if i - j > maks:
                    maks = i - j
                    rem = [j,i]
    sol = ""
    for i in range(rem[0],rem[1]+1):
        sol += S[i]
    print(sol,maks,rem)
    return sol

def palindrom(S):
    return fun(S)

def palindrom2(S):
    n = len(S)
    maks = 1
    rem = [0,0]
    for i in range(n):
        for j in range(i):
            #print(i,j)
            if is_palindrom(S,j,i):
                if i - j + 1 > maks:
                    maks = i - j + 1
                    rem = [j,i]
    sol = ""
    for k in range(rem[0],rem[1]+1):
        sol += S[k]
    return sol

runtests ( palindrom )