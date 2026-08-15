def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        j = i - 1
        k = tab[i]
        while j >= 0 and tab[j]>k:
            tab[j+1]=tab[j]
            j=j-1
        tab[j+1]=k
t = [5,4,3,2,1]
print(t)
tri_insertion(t)
print(t)


