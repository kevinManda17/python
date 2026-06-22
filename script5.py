b=2
k=6
n=23
s=0
i=k-1
q=n
while q!=0 and i>=0 :
    s=s+(q%b)*b**(k-1-i)
    print(q%b,end="")
    q=q/b
    i=i-1