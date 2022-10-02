print("Adja meg a háromszög három oldalát cm-ben: \n")
a=int(input("a oldal (cm): "))
b=int(input("b oldal (cm): "))
c=int(input("c oldal (cm): "))
if (a+b)>=c and (b+c)>=a and (a+c)>=b:
    print("Az", a,",", b, "és" ,c, "oldalú háromszög szerkeszthető.")
else:
    print("Az", a,",", b, "és" ,c, "oldalú háromszög NEM szerkeszthető.")