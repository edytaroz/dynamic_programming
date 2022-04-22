def fun(T):
    n = len(T)
    suma = 0
    for i in range(n):
        suma += T[i]
    B = [[inf for _ in range(suma+1)] for _ in range(n+1)]
    B[0][T[0]] = 1
    maks = 0
    for i in range(n):
        maks += T[i]
        for k in range(maks+1):
            if B[i][k] != inf:
                for j in range(T[i]):
                    if i + j <= n:
                        B[i+j][k-j] = min(B[i+j][k-j],B[i][k]+1)
    return B[n-1][suma-1] - 1
