# -*- coding: utf-8 -*-
"""Exercices_auditoire.ipynb



   

1. Corriger le code source suivant et calculer la valeur de S et écrire la liste complète T après utilisation de la fonction p1
"""

def p1(T):
    a = 3
    b = [2,7,3]
    T[b[0]] += T[a]
    return T
s = p1([5,6,8,1])

"""2. Corriger le code source suivant et calculer la valeure de s"""

def p2(a,b):
    c = a + b
    return c
s = p2(8, "3")

"""3. Calculer les valeurs S1, S2, S3:
- Que fait cette fonction
- Comment la réécrire simplement
"""

def p3(m,n):
    q=0
    while n <= m:
        q+=1
        m-=n
    return q
s1 = p3(7,3)
s2 = p3(5,6)
s3 = p3(17,2)

"""4. Corriger le code source suivant:
- Que fait cette fonction
- Reecrire la fonction avec votre propre raisonnement

def p4(n):
    retourne (n % 2 = 0)

5. Corriger le code source de la fonction p5 et calculer la valeur de s :

def p5(T):
    s = 0
for x in range(len(T)):
    if T[x] % 2 == 0:
        s += [x]
        r = len(s)
return s[r-1]
s1 = p5([7,4,9,6,5])
"""

def p5(T):
    #s = 0
    s=0
    for x in range(len(T)):
        if T[x] % 2 == 0:
            s +=T[x]
            r = len(s)
    return s[r-1]
s1 = p5([7,4,9,6,5])

"""6. Ecrire la présente fonction autrement"""

def p6(a,b):
    return a > b
p6(7,5)

"""7.  Tester le code et dites que font les fonctions p7 et p8 ?"""

def p7(m, n):
    return m % n == 0
def p8(d, n):
    return n % d == 0
p7(8,2)
p8(2,8)

"""10 Mars 2023

Calculer la valeur de s1, s2 et s3 :
"""

def p14(n):
    u=1
    for i in range(n):
        u=1-2*u
    return u
s1 = p14(9)
s2 = p14(3)
s3 = p14(10)
print(f'S1:{s1}, S2:{s2}, S3:{s3}')

for i in range(5):
    print(i)

"""8. Corriger le code source de la fonction p9 si possible et répondez aux questions suivantes:
    1. Calculer les valeurs s1,s2,s3,s4
    2. Que fait la fonction p9
    3. Utilisez la boucle while pour réécrire la fonction p9
"""

def diviseur(n):
    s =list()
    for x in range(n+1,0,-1):
        if n % x == 0:
            s+=x
    return s
s1 = p9(7)
s2 = p9(15)
s3 = p9(21)
s4 = p9(12)
s1

"""11 Mars 2023

1. Modifier la fonction diviseur pour en faire la fonction premier
La fonction premier retourne True si la valeur en paramètre est
un NOMBRE PREMIER, sinon elle renvoie FALSE.
"""

def diviseur(n):
    s =0
    for x in range(n,0,-1):
        if n % x == 0:
            s+=1
    if s== 2 :
        return True
    else : 
        return False
diviseur(6)



"""2. Corriger le code suivant si necéssaire, 
trouver les valeurs de s1 et s2 et dites que fais la fonction p11
"""

def p11(v):
    g = v[0]
    for x in v:
        if x > g:
            g = x
    return g
s1 = p11([8,7,5,9,1,3])
s2 = p11([6,5,3,7,8])

"""3. Calculer la valeur de s1 et s2 en tenant compte de la fonction suivante 
    - Que fait cette fonction
    - Ecrire cette fonction en une ligne de code
"""

def p12(a,b):
    return a in b
p12(4, [7,8,3,1,9])
#s2 = p12(3, [7,8,3,1,9])

"""4. Corriger le code source suivant si possible, ensuite calcule la valeur de s1 et
s2
"""

def p16(a, b):
    r = []
    for i in (a):
        f = True
        for j in b:
            if i == j:
                f = False
        if f:
            r += [i]
    return r
s1 = p16([4, 5, 3], [2, 5, 1, 4])
s2 = p16([2, 5, 1, 4], [4, 5, 3])

"""Calculer la valeur de s1 et s2 :"""

def p17(T,g,d):
    aux = T[d]
    for k in range(d,g,-1):
        T[k] = T[k-1]
        T[g] = aux
    return T
def p18(T,g,d):
    aux = T[g]
    for i in range(g,d):
        T[i] = T[i+1]
        T[d] = aux
    return T
s1 = p17([8,5,7,6,3],1,3)
s2 = p18(s1,1,3)

"""11 Mars Les Matrices

12. Ecrire une fonction nommée recherche qui va prendre en paramètre une matrice et le nombre recherché en second paramètre. la fonction retourne la position exacte du nombre recherché.

13. Ecrire une fonction qui recois en paramettre une matrice et retourne sa transposée

14. Ecrire une fonction (renversement) qui retourne un mot pris en paramètre.
"""

def renversement(k):
    l=len(k)
    t=''
    for i in range (l-1,-1,-1):
        t+=k[i]
    return t
k='bonjour'
renversement(k)

"""15. En utilisant la fonction renversement, écrire une fonction qui permet de vérifier si un mot est un palindrome, qui renvoie True ou False selon qu'il s'agisse d'un palindrome ou pas.

16. En utilisant les fonctions python ord et char:
Ecrire une fonction qui vas crypter chacun des mots mis en paramètre.
"""

s=ord('n') # donne 101
y=chr(101)
s

a='bonjour'
a[3]
a+='s'
a



"""17. Calculer la valeur de s1, s2 et s3, ensuite expliquer ce que fait la fonction
suivante :
"""

def p13(t, n, a):
    h = len(t)
    for i in range(h):
        if t[i] == a:
            t[i] = n
    return t
s1 = p13([4,5,1,0,8], 4, 3)
s1 = p13([4,5,1,0,8], 3, 4)
s1 = p13([4,8,1,0,8], 7, 8)

"""Corriger le code source suivant si possible, ensuite calcule la valeur de s1 et
s2
"""

def p16(a, b):
    r = []
    for i in (a):
        f = True
    for j in b:
        if i == j:
            f = False
        if not f:
            r += [i]
    return r
s1 = p16([4, 5, 3], [2, 5, 1, 4])
s2 = p16([2, 5, 1, 4], [4, 5, 3])

def crypt(mot):
    new=''
    for i in mot: 
        c=ord(i)+8
        new+=chr(c)
    return new
b='bonjour'
s=crypt(b)
print(s)

def decryp(a):
    taille=len(a)
    res=""
    for i in range(0, taille):
        eq=ord(a[i])
        eq-=4
        res+=chr(eq)
    return res
decryp("HtovsuZ")

M3=M2
def initialisation(M):
      for i in range(len(M)):
           for j in range(len(M)):
              M3[i][j]=0
      return M3
#M3=initialisation(M2)
for i in range(len(M1)):
      for j in range(len(M2)):
         M3[i][j]=M1[i][j]+M2[i][j]
         #print(f'M1 vaut {M1[i][j]} M2 vaut {M2[i][j]}')
      #break
print(M3)

def diviseur (n):
    compteur=0
    for i in range(1, n+1, 1):
        if n % i == 0:
            compteur+=1
    if compteur > 2:
        return False
    else:
        return True
diviseur(17)

"""13 Mars 2023

Trouver la valeur de s1
"""

def fonction2(a,b):
    if b == 0:
        return a
    else:
        r = a % b
    return fonction2(b,r)
s1=fonction2(42,9)

"""1. Ecrire une fonction permettant de vérifier la validité d'une adresse mail en fonction de son format.

2. Ecrire une fonction cryptage permettant de crypter le mot 'Kubernetes' en fonction de la règle de l'ordre inverse du mot pris en paramètre et renvoie la somme du correspondant ASCII de chacunes des lettres résultantes ainsi que la fonction decrypt.

3. Ecrire une fonction qui réalise le produit matriciel de deux matrices
"""

M1=[[1,2,3,4],
   [7,9,10,11],
   [4,12,10,3],
   [0,1,5,7]]

M2=[[9,5,2,1],
   [7,3,1,9],
   [17,24,6,31],
   [1,8,9,6]]

"""3. Ecrire une fonction python PIN_verif, permettant de vérifier si le code PIN est correcte (correspond à 8749).
    - L'utilisateur est invité à insérer le PIN
    - L'utilisateur a droit à 7 tentatives
    - A la 7ème tentative, si l'utilisateur échoue, le message 'Vous etes un voleur' apparait.

4. CAlculer la valeur de s1 et s2
"""

def p17(T,g,d):
    aux = T[d]
    for k in range(d,g,-1):
        T[k] = T[k-1]
        print(T[k])
        T[g] = aux
    return T
def p18(T,g,d):
    aux = T[g]
    for i in range(g,d):
        T[i] = T[i+1]
        T[d] = aux
    return T
s1 = p17([8,5,7,6,3],1,3)
#s2 = p18(s1,1,3)
s1

"""5. Calculer la valeur de s1, s2 et s3 :"""

def fonction1(x,y):
    if x == 0 and y == 0:
        return 0
    elif y == 0:
        return 1 + fonction1(0,x-1)
    else:
        return 1 + fonction1(x+1,y-1)
def fonction2(a,b):
    if b == 0:
        return a
    else:
        r = a % b
    print(f'a : {a}  b : {b}  r : {r}')
    return fonction2(b,r)
#s1 = fonction1(5,8)
s2 = fonction2(150,11)
#s2 = fonction2(42,9)

"""14 Mars 2023"""

def fonctionp(T,g,d):
    aux = T[d]
    for k in range(d,g,-1):
        print(f'k: {k} aux:{aux},g:{g}, T[k]:{T[k]}, T[g]:{T[g]}, T:{T}')
        T[k] = T[k-1]
        T[g] = aux
    return T
s1 = fonctionp([8,5,7,6,3],1,3)
s1

"""2. trouver la valeur de s2"""

def p18(T,g,d):
    aux = T[g]
    for i in range(g,d):
        T[i] = T[i+1]
        T[d] = aux
    return T
s2 = p18(s1,1,3)
s2

"""2. Ecrire une fonction cryptage permettant de crypter le mot 'Kubernetes' en fonction de la règle de l'ordre inverse du mot pris en paramètre et renvoie la somme du correspondant ASCII de chacunes des lettres résultantes ainsi que la fonction decrypt."""

def renversement(k):
    l=len(k)
    t=""
    for i in range(1-1,-1):
     t=k(i)
     return t
k="kubernetes"
renversement(k)

"""
1. FAites le pseudo code
2. proposer un code python"""

M1=[[1,2,3,4],
   [7,9,10,11],
   [4,12,10,3],
   [0,1,5,7]]

M2=[[9,5,2,1],
   [7,3,1,9],
   [17,24,6,31],
   [1,8,9,6]]

"""Jeudi 16 Mars 2023

1. Ecrire une fonction python qui demande à l'utilisateur d'écrire un nombre binaire et la fonction renvoie son équivalent HEXADECIMAL.
    1. Vérifier la saisie de l'utilisateur en lui demandant de resaisir le nombre binaire en lui indiquant la faute.
    2. La fonction portera votre nom et retournera l'équivalent HEXA.

2. Ecrire un algorithme (Pseudo code +  code python) qui demande à l'utilisateur de saisir 7 nombres entiers et les affiches.
Exemple:\n

    Inscrire le nombre 1
    Inscrire le nombre 2
    Inscrire le nombre 10
    les nombres inscrits sont : 1 2 12 41 74 85 41
NB: vérifier la saisie.

3. Ecrire une fonction python qui demande à l'utilisateur de saisir du texte et detecte dans le texte des  minuscules, les affiches et retrourne l'équivalent corrigé en majuscule.

4. Ecrire une fonction python qui compte le nombre d'occurence d'une lettre prise en paramètre dans un texte.

5. Ecrire une fonction qui imprime(affiche) la liste d'eléments dupliqués d'une liste qui lui est passée en paramètre.

6. Ecrire une fonction python qui recois une liste en paramètre et renvoie la valeure la plus grande de la liste.(Faire de même pour l'élément le plus petit).

7. Ecrire une fonction qui recois en paramètre une liste de 10 éléments (vérifier) et places les éléments d'indice 2 à 5 en fin de liste.

8. Ecrire une fonction python qui effectue une permutation circulaire droite de ses éléments.

9. Ecrire une fonction qui recoit en paramètre deux listes et retourne une liste 3 regroupant les éléments différents de deux.
"""

def bon(n):
    r=''
    for i in n:
        if ord(i)>=97 and ord(i)<=122:
            print(i)
            r+=chr(ord(i)-32)
        else:
            r+=i
    return r
b=input('Saisir le texte :')
print(bon(b))
