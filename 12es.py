


hany=6
szam=13

while hany != 10001:

    szam+=1
    osztokszama=0

    for i in range(1,szam+1):
        if szam%i==0:
            osztokszama+=1

        if osztokszama==2:
            hany+=1

if hany==10001:
    print(szam)







#Végig menni a számokon egészen addig amíg 10001. prímet meg nem találtuk
#megszámolni, hogy az adott számnak hány osztója van
#ha pontosan 2 db osztója van megnövelni a prímek számát 1-el
#ha a prímek száma 10001 returnolni a számot
