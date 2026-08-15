def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

resultat = factorielle(4)
print(f'4! = {resultat}')
