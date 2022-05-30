from zad5ktesty import runtests


def fun(A):
    n = len(A)
    a = 0
    b = n - 1
    k = 0
    rem1 = 0
    rem2 = 0
    l =[]
    for i in range(n):
        #print(a,b)
        if a + 1 < b - 1:
            if A[a] + A[b-1] > A[a+1] + A[b]:
                if k % 2 == 0:
                    rem1 += A[a]
                    l.append(A[a])
                    a += 1
                else:
                    rem2 += A[a]
                    a += 1
            else:
                if k % 2 == 0:
                    rem1 += A[b]
                    l.append(A[b])
                    b -= 1
                else:
                    rem2 += A[b]
                    b -= 1
            k += 1
        else:
            if A[a] > A[b]:
                if k % 2 == 0:
                    rem1 += A[a]
                    l.append(A[a])
                    a += 1
                else:
                    rem2 += A[a]
                    a += 1
            else:
                if k % 2 == 0:
                    rem1 += A[b]
                    l.append(A[b])
                    b -= 1
                else:
                    rem2 += A[b]
                    b -= 1
            k += 1
    print(A)
    print(l)
    return max(rem1,rem2)

def rek(A,i,sum1,sum2):
    if i == len(A) - 1:
        return max(sum1,sum2)
    else:
        return max(rek(A,i+1,sum1+A[i],sum2),rek(A,i+1,sum1,sum2+A[i]))

def garek ( A ):
    print(rek(A,0,0,0))
    #Tutaj proszę wpisać własną implementację
    return fun(A)

runtests ( garek )
