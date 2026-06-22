#coding:utf-8


f"print{elm} "

"""
[<expression> for in <list> ]
[<expression> for in <list> if <condition> ]
[ [[<expression> for in <list>]]for in <list>]

"""
li= [1,2,3,4,5,6,7,8,9]

for elm in li :
    # print(elm)
    pass
print("---------print special---------\n")

[print(elm) for elm in li ]

print("---------print special---------\n")

tli=[9,8,7,6,5,4,3,2,1]

nli =[]

[nli.append(i) for i in tli]
# for i in nli :
#     print(i)

print("---------print special---------\n")

print(nli)
print(li)


print("---------print special---------\n")

print(id(nli))
print(id(li))

print("---------print special---------\n")

xli = [True if i%2 == 0 else False for i in li]
print(xli)

print("---------print special---------\n")

#une liste en comprehension

xli= [n +1 for n in tli if n % 2==0 ]

print(xli)
xli= [n +1 for n in tli if n % 2==0 if n > 4]

print(xli)

print("---------print special---------\n")

list_name= ["kevin" ,"manda", "Mubenga", "olivier"]

lst_name= [name for name in list_name if name == "kevin"]

print(lst_name)

print("---------print special---------\n")

xli = [True if i%2 == 0 else False for i in xli]
print(xli)

print("---------print special---------\n")

lli = [
    [1,2,3,4],
    [10,20,30,40],
    [100,200, 300, 400]
]
nlli =[]

for subli in lli :
    for n in subli :
        nlli.append(n)
print(f"le nlli : {nlli}")
print(f"le lli :{lli}")


# une liste en comprehension daans une liste en comprehension

wli= [
    [1,2,3,4],
    [10,20,30,40],
    [100,200, 300, 400]
]

nwli =[y for subli in wli for y in subli]


print(F"le wli: {wli}")
print(F" le nwli : {nwli}")

