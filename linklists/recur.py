def fic(n):
    if n == 0:
        return 1

    return n* fic(n-1)

ffic = fic(5)

print(ffic)



# fabunacci

#formula for nth fabonacci number is F(n) = F(n-1) + F(n-2)
def feb(n):

    if n == 0:
        return 0

    return feb(n-1) + feb(n-2)

feba = feb(5)
print(feba)