import numpy as np 

#filtering numpy arrays with Boolean index lists 
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
np3 =np.array([[1,2,3],[4,5,6],], [[7,8,9], [10,11,12]])

x= [True ,True , False , False , False , False ,False ,False ,False , False ,]
print(np1)
print(np1[x])

filtered = []
for i in np1 :
    if i % 2 == 0 :
        filtered.append(True)
    else :
        filtered.append(False) 

for x in np.nditer(np3):
    print(x)