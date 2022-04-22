def forest(T):
    n = len(T)
    B = [0 for _ in range(n)]
    B[0] = T[0]
    B[1] = T[1]
    B[2] = max(B[1],B[0]+T[2])
    for i in range(3,n):
        B[i] = max(B[i-2]+T[i],B[i-3]+T[i])
    return B[n-1]
