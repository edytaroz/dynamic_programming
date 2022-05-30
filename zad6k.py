from zad6ktesty import runtests 

def haslo ( S ):
    print(S)
    if len(S) == 1 or len(S) == 0:
        return 1
    if "00" in S:
        return 0
    if len(S) == 2:
        if "0" in S:
            return 1
        else:
            if S <= "26":
                return 2
            return 1
    tab = [0 for _ in range(len(S))]
    if "0" in S:
        if S[0] == "0":
            return 0
        tab[0] = 1
        if S[0] + S[1] <= "26":
            if S[1] != "0":
                tab[1] = 2
            else:
                tab[1] = 1
        else:
            if S[1] == "0":
                return 0
            tab[1] = 1
        for i in range(2, len(S)):
            if S[i - 1] + S[i] <= "26":
                if S[i-1] != "0":
                    if S[i] != "0":
                        tab[i] = tab[i - 1] + tab[i - 2]
                    else:
                        tab[i] = tab[i-2]
                else:
                    tab[i] = tab[i-1]
            else:
                if S[i] != "0" and S[i-1] != "0":
                    tab[i] = tab[i - 1]
                elif S[i] != "0" and S[i-1] == "0":
                    tab[i] = tab[i-1]
                else:
                    return 0
        return tab[len(S) - 1]
    else:
        tab[0] = 1
        if S[0]+S[1]<="26":
            tab[1] = 2
        else:
            tab[1] = 1
        for i in range(2,len(S)):
            if S[i-1]+S[i] <= "26":
                tab[i] = tab[i-1] + tab[i-2]
            else:
                tab[i] = tab[i-1]
        return tab[len(S)-1]

runtests ( haslo )