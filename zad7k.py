from zad7ktesty import runtests 
from queue import Queue
def korzenie(T,D):
    n = len(T)
    m = len(D)
    tab = [0 for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tab[i] += T[j][D[i]]
        rem1 = D[i]
        rem2 = D[i]
        flag1 = True
        flag2 = True
        while flag1:
            rem1 -= 1
            if rem1 >= 0 and rem1 < len(T[0]):
                flag1 = False
                for j in range(n):
                    tab[i] += T[j][rem1]
                    if T[j][rem1] != 0:
                        flag1 = True
            else:
                flag1 = False
        while flag2:
            rem2 += 1
            if rem2 >= 0 and rem2 < len(T[0]):
                flag2 = False
                for j in range(n):
                    tab[i] += T[j][rem2]
                    if T[j][rem2] != 0:
                        flag2 = True
            else:
                flag2 = False
    return tab

def is_poss(G,u):
    n = len(G)
    m = len(G[0])
    t = [[1,0],[-1,0],[0,1],[0,-1]]
    l = []
    for i in range(4):
        w = u[0] + t[i][0]
        k = u[1] + t[i][1]
        if w >= 0 and k >= 0:
            if w < n and k < m:
                if G[w][k] != 0:
                    l.append([w,k])
    return l

def bfs(G,D):
    n = len(G)
    m = len(G[0])
    Q = Queue()
    tab = [0 for _ in range(len(D))]
    vis = [[False for _ in range(m)] for _ in range(n)]
    par = [[-1 for _ in range(m)]for _ in range(n)]
    d = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(len(D)):
        s = (0,D[i])
        vis[0][D[i]] = True
        Q.put(s)
        suma = G[s[0]][s[1]]
        while not Q.empty():
            u = Q.get()
            pr = is_poss(G,u)
            for v in pr:
                if not vis[v[0]][v[1]]:
                    suma += G[v[0]][v[1]]
                    vis[v[0]][v[1]] = True
                    d[v[0]][v[1]] = d[u[0]][u[1]] + 1
                    par[v[0]][v[1]] = u
                    Q.put(v)
        tab[i] = suma
    return tab


def ogrodnik (T, D, Z, l):
    n = len(D)
    #k = korzenie(T,D)
    k = bfs(T,D)
    tab = [[0 for _ in range(l+1)] for _ in range(n)]
    for i in range(k[0],l+1):
        tab[0][i] = Z[0]
    for z in range(l+1):
        for i in range(1,n):
            tab[i][z] = tab[i-1][z]
            if z - k[i] >= 0:
                tab[i][z] = max(tab[i][z],tab[i-1][z-k[i]]+Z[i])
    return tab[n-1][l]

runtests( ogrodnik, all_tests=True )
