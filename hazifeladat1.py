#1.feladat
#betuk
szoveg = input("Adjon meg egy mondatot: \n")
d = {}
for i in szoveg:
    d[i] = szoveg.count(i)
print("Betűk gyakorisága:",d)
#visszafele
szoveg2 = szoveg [::-1]
print("Fordítva: ",szoveg2)
#listaba rendezes
print("Listába rendezve szavanként: ",szoveg.split())


#2.feladat
x = float(input("Adjon meg egy számot és egy mértékegységet (сm/inch):\n"))
meret = input()
valto = 2.54
if(meret == "cm"):
    x = x * valto
    print(x)
elif (meret == "inch"):
    x = x  / valto
    print(x)
else:
    print("nem megfelelo mértékegység!")