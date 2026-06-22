from math import sqrt
print("resoudre l'equation:aX²+bX+cX=0 ")
a=int(input("entrez une valeur de a: "))
b=int(input("entrez une valeur de b: "))
c=int(input("entrez une valeur de c: "))
mbr=int(input("entrez un nombre: "))
print("votre equation est : ",a,'X²+',b,'X+',c,'=',mbr)
# if mbr!=0 and c<0:
#     c=c+mbr
#     mbr=0
#     pass
#     print("votre equation est : ",a,'X²+',b,'X+',c,'=',mbr)
if mbr<0 or mbr>c and mbr!=0 and mbr<c:
    c=c+mbr
    mbr=0
    print("votre equation est : ",a,'X²+',b,'X',c,'=',mbr)
    pass 
else:
    c=c+mbr
    mbr=0
    print("votre equation est : ",a,'X²+',b,'X+',c,'=',mbr)
    pass
print("resoudre l'equation du segond degre !")
delta=b**2-4*a*c
print("delta est :",delta)
if delta>0:
    del_racines=sqrt(delta)
    B=-b
    num=B+del_racines
    num2=B-del_racines
    den=2*a
    x1= (num/den)
    x2= (num2/den)
    print("-b est:",B)
    # print(num2)
    # print(num)
    print("vos racines sont x1:",x1,"x2:",x2)
elif delta==0:
    B=-b
    den=2*a
    x1=x2=(B/den)
    print("vos racines sont x1:",x1,"x2:",x2)
else:
    print("pas des racines,donc pas de solution !")