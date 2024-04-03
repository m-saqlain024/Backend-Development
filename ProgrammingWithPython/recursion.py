def factorail(n):
    if n<0:
        return 0
    else:
        factor = 1
        for i in range(1,n+1):
            factor=factor*i
        return factor

print(factorail(4))