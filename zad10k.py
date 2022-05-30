from zad10ktesty import runtests
from math import sqrt
from math import floor
def fun(N):
    i = floor(sqrt(N))
    sol = []
    tab = [0 for _ in range(N+1)]
    for j in range(1,N+1):
        min = -1
        for k in range(1,i+1):
            if j - k*k >= 0:
                if min < 0 or tab[j-k*k] + 1 < min:
                    min = tab[j-k*k] + 1
        tab[j] = min
    rem = N
    sum = 0
    for j in range(i,-1,-1):
        if rem - j*j >= 0:
            if tab[rem-j*j] + 1 == tab[rem]:
                sol.append(j)
                rem = rem - j*j
                sum += j*j
    sol.sort()
    if sum != N:
        for j in range(len(sol)-1,-1,-1):
            if sum + sol[j]*sol[j] <= N:
                flag = True
                while flag:
                    sol.append(sol[j])
                    sum += sol[j]*sol[j]
                    if sum + sol[j]*sol[j] > N:
                        flag = False
    sol.sort()
    return sol


def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    return fun(N)


runtests( dywany )

