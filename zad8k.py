from zad8ktesty import runtests 

def lis1(s,t):
    n = len(s)
    m = len(t)
    maxi = 0
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if s[i] == t[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    return F[maxi]

def fun(s,t):
    n = len(s)
    m = len(t)
    tab = [0 for _ in range(n)]
    pos = [0 for _ in range(n)]
    flag = False
    for j in range(m):
        if not flag:
            if s[0] == t[j]:
                pos[0] = j
                flag = True
    for i in range(1,n):
        #is letter in string
        flag = False
        rem = 0
        fl = False
        for j in range(m):
            if not flag:
                if s[i] == t[j]:
                    rem = j
                    fl = True

        if flag:
            tab[i] = tab[i-1] + 1
        else:
            tab[i] = tab[i-1]
    print(tab[n-1],m,n)
    return abs(m - n) + (n - tab[n-1])

def fun2(s,t):
    n = len(s)
    m = len(t)
    maxi = 0
    F = [1 for _ in range(n+m)]
    P = [-1 for _ in range(n+m)]
    for i in range(1, n):
        for j in range(m):
            if s[i] == t[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    print(n,m)
    return F[maxi] + abs(m - n)

def fun3(s,t):
    n = len(s)
    m = len(t)
    tab = [[0 for _ in range(m+1)] for _ in range(2)]
    for i in range(m+1):
        tab[0][i] = i
    for i in range(1,n+1):
        for j in range(m+1):
            if j == 0:
                tab[i%2][j] = i
            elif t[j-1] == s[i-1]:
                tab[i%2][j] = tab[(i-1)%2][j-1] + 1
            else:
                tab[i%2][j] = 1 + max(tab[(i-1)%2][j],tab[i%2][j-1],tab[(i-1)%2][j-1])
    return tab[n%2][m]


def EditDistDP(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    DP = [[0 for i in range(len1 + 1)]
          for j in range(2)]

    for i in range(0, len1 + 1):
        DP[0][i] = i

    for i in range(1, len2 + 1):

        for j in range(0, len1 + 1):

            if (j == 0):
                DP[i % 2][j] = i

            elif (str1[j - 1] == str2[i-1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]

            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                    min(DP[i % 2][j - 1],
                                        DP[(i - 1) % 2][j - 1])))


    return DP[len2 % 2][len1]

def fun4(s,t):
    n = len(s)
    m = len(t)
    tab = [[0 for _ in range(m)] for _ in range(n)]
    if s[0] != t[0]:
        tab[0][0] = 1
    flag = False
    for i in range(1,n):
        if s[i] == t[0]:
            if not flag:
                tab[i][0] = tab[i-1][0]
                flag = True
            else:
                tab[i][0] = tab[i-1][0] + 1
        else:
            tab[i][0] = tab[i-1][0] + 1
    flag = False
    for i in range(1,m):
        if s[0] == t[i]:
            if not flag:
                tab[0][i] = tab[0][i-1]
                flag = True
            else:
                tab[0][i] = tab[0][i-1] + 1
        else:
            tab[0][i] = tab[0][i-1] + 1
    for j in range(1,m):
        for i in range(1,n) :
            if s[i] != t[j]:
                tab[i][j] = min(tab[i-1][j],tab[i-1][j-1],tab[i][j-1]) + 1
            else:
                tab[i][j] = tab[i-1][j-1]
    print(s)
    print(t)
    return tab[n-1][m-1]

def napraw ( s, t ):
    return fun4(s,t)
    #return fun3(s,t)

runtests ( napraw )