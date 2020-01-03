def dbl_linear(n):
    u = [1]
    for x in range(0, n):
        x = u[x]
        u.append(x*2+1)
        u.append(x*3+1)
    u = list(set(u))
    u.sort()
    print(u[100])

dbl_linear(471)