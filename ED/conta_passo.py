def conta_passo (n):
    cont = 0
    while n != 1:
        if (n % 2 == 0 ):
            cont += 1
            n = n//2
        else:
            cont +=1
            n = 3*n+1
    return cont
