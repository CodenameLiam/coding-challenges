def solve(s): 
    p = 0 

    while p <= len(s) // 2:
        q = len(s) - p - 1
        if s[p] != s[~p]:
            if s[p+1:q+1] == s[q:p:-1]:
                return p
            elif s[p:q] == s[p:q][::-1]:
                return q
            else:
                return -1
        p += 1

    return -1


print(solve('aaaaaaba'))