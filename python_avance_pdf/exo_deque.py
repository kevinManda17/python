from collections  import deque 

"""@KevinManda"""

d = deque([1,2,3])
print(d)
d.append(4)
print(f"apres l'ajout : {d}")
d.appendleft(0)
print(f"l'ajout a gauche: {d}") 
d.popleft()
print(f'on voit ce que ca donne : {d}')
r = deque([0,1,2,3,4])
r.pop() 
print(f"R est : {r}")

