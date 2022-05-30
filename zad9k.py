from zad9ktesty import runtests

def suma(T,q,g,i):
    d = max(q, g)
    count = [[0 for _ in range(i+1)] for _ in range(d+1)]
    rem =[[False for _ in range(i+1)] for _ in range(d+1)]
    l = []
    for j in range(i+1):
        count[0][j] = 0
        rem[0][j] = True
    for j in range(1,d+1):
        count[j][0] = -1
        rem[j][0] = False
    for j in range(1,d+1):
        for k in range(1,i+1):
            rem[j][k] = rem[j-1][k]
            count[j][k] = count[j-1][k]
            if j >= T[k-1]:
                rem[j][k] = (rem[j][k] or rem[j - T[k-1]][k-1])
                if rem[j][k]:
                    count[j][k] = max(count[j][k-1],1+count[j-T[k-1]][k-1])
    a = d
    b = i
    while a >= 0 and b > 0:
        if a - T[b-1] >= 0 and count[a][b] == 1 + count[a-T[b-1]][b-1]:
            l.append(b-1)
            b -= 1
            a -= T[b]
        elif count[a][b] == count[a-1][b]:
            a -= 1
        elif count[a][b] == count[a][b-1]:
            b -= 1
    l.sort()
    print(l)
    print(i)
    if len(l) == 0:
        for j in range(i):
            l.append(j)
        return l
    if i - 1 == l[len(l)-1]:
        return l
    else:
        r = []
        k = 0
        for j in range(i):
            if k < len(l) and l[k] == j:
                k += 1
            else:
                r.append(j)
        return r


def prom1(T,d,g):
    print(T)
    print(d,g)
    maxs = 0
    d1 = 0
    g1 = 0
    for i in range(len(T)):
        if fun(T,i,d,g) is False:
            maxs = i
            break
        else:
            d1 = d
            g1 = g
    print(d1,g1)
    t = suma(T,d1,g1,maxs)
    return t

def fun(T,i,L,R):
    if L< 0 or R < 0 :
        return False
    elif i < 0:
      return True
    else: return fun(T,i-1,L-T[i], R) or fun(T,i-1,L,R-T[i])

def prom(P, g, d):
    return prom1(P,g,d)

runtests ( prom )
