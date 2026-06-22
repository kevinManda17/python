a =[[11,12,13,54],
    [21,22,23,12],
    [31,32,33,23],
    [41,42,43,12]
]

b=[[42,4,45,7],
   [58,65,1,11],
   [31,41,2,85],
   [22,11,43,17]
]
r= a[0][0]+b[0][0]
print(r)

k=1
for i in range(0,4):
    
    for j in range(0,4):
        c=a[i][j]+b[i][j]
        print(f" #id {k} la matrice C, la somme de A et B : {c}")
        # print(f"""[{c}]""")
        k +=1

        r= a[0][0]+b[0][0]
# print(r)

n=0
for i in range(0,n):
    for j in range(0,4):
        # pass
        # print(c[i][j])
        c=a[i][j]+b[i][j]
        print(f"""[{c}","]""")
        n +=1
        
