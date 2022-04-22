def fun(T):
    n = len(T)
    A = [1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if T[j][0] <= T[i][0] and T[j][1] >= T[i][1]:
                A[i] = max(A[j]+1,A[i])
    return max(A)
