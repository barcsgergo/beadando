

#egyik számot elindítjuk 999-ről
#másik számot 999-ről lépegetjük lefelé
#megvizsgáljuk az adott 2 szám szorzatát, megnézzük, hogy a szorzat és a szorzat fordítottja ugyanaz-e (ehez stringgé kell alakítani)
#ha igen akkor az aktuális i-t és j-t és szorzatot eltároljuk új változókba, hogy ne vesszenek el
#ezután kilépünk a ciklusból break-kel
#mivel dupla ciklus fut éppen ezért kissé bonyolultabb a dolog, ezért kell a végére az a furcsaság, mert anélkül a külső ciklus tovább futna

for i in range (999,99,-1):
    for j in range (999,99,-1):

        szorzat=i*j
        if str(szorzat) == str(szorzat)[::-1]:

            sz=str(szorzat)
            a=i
            b=j
            break

    else:
        continue
    break

print ('{} * {} = {}'.format(a,b,sz))