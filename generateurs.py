def generator():
    yield "a"
    yield "b"
    yield "c"

i = generator()
for k in i  :
    print(k)

def generator1(n):
    for t in range(n):
        if t == 5 :
            print(f"On est deja au {t} tour ")
        yield t+1

n=generator1(int(input("Entrez n: ")))
for e in n:
    print(e)