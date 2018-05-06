#csinálok először egy prim fv-t, ami mindig meg fogja vizsgálni a későbbiekben, hogy prím-e az aktuális szám

#Végig menni a számokon egészen addig amíg 10001. prímet meg nem találtuk

#a feladatból tudjuk, az első 6 prímet és az aktuális számot, így elég attól a számtól indítani a ciklust
#amig a hany változó nem éri el a 10001-et addig a szam változóhoz hozzá adunk 1-et és megvizsgáljuk, hogy prím-e
#ha igen, akkor a hany-hoz hozzá adunk 1-et
#ha a hany 10001 kiiratni a számot

#jól működik a program és kiírja, hogy 104743 viszont nagyon lassan fut (~40-50 másodperc)

def prim_e(n):
    if n==2:
            return 'Prim'

    for i in range(2,n):
        if n%i == 0:
            return 'Nem Prim'
    return 'Prim'


hany=6
szam=13

while hany != 10001:

    szam+=1
    if prim_e(szam)=='Prim':
        hany+=1


print(szam)











