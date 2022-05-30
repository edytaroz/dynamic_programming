from zad3ktesty import runtests


def fun(T,k):
    n = len(T)
    tab = [[0,0] for _ in range(n)]
    if k == n:
        return min(T)
    elif k == 1:
        suma = 0
        for i in range(n):
            suma += T[i]
        return suma
    else:
        mini = T[0]
        rem = 0
        for i in range(k):
            if T[i] <= mini:
                mini = T[i]
                rem = i
        tab[0] = [mini,rem]
        for i in range(1,n-k):
            if tab[i][0] < T[i+k]:
                tab[i] = [mini,rem]
            else:
                tab[i] = [T[i+k],i+k]

def fun2(T,k):
    n = len(T)
    if n == k:
        return min(T)
    if k == 1:
        suma = 0
        for i in range(n):
            suma += T[i]
        return suma
    tab = [float('inf') for _ in range(n)]
    for i in range(k):
        mini = T[i]
        #for j in range(i):
            #if T[j] < mini:
                #mini = T[j]
        tab[i] = mini
    for i in range(k,n):
        mini = T[i]
        for j in range(i-k+1,i):
            if T[j] < mini:
                mini = T[j]
        tab[i] = mini
    suma = 0
    i = n - 1
    #print(T)
    #print(tab)
    #print(k)
    while i >= 0:
        suma += tab[i]
        i -= k
    i = n - 1
    sol = [float('inf') for _ in range(n)]
    '''''
    for i in range(k):
        mini = min(sol)
        sol[i] = min(tab[i],mini)
    for i in range(k,n):#min suma do danego punktu
        sum1 = tab[i] + sol[i]
        for j in range(i-k+1,i-1):
            if sum1 > tab[j] + sol[i-1]:
                sum1 = tab[j] + sol[i-1]
        sol[i] = sum1
    '''
    suma = 0
    while i > 0:
        if i < k:
            mini = tab[i]
            for p in range(i):
                if tab[p] < mini:
                    mini = tab[p]
            suma += mini
            i = -1
        else:
            suma += tab[i]
            j = i
            while j >= 0 and T[j] != tab[i]:
                j -= 1
            i = j - 1
            #i = j
            if j == 0:
                i = -1
                #suma += tab[j]
    if n < 100:
        print(T)
        print(tab)
        print(sol)
    return suma

def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    return fun2(T,k)
    #return 0
    
runtests ( ksuma )
