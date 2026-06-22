import numpy as np 

#copy vs view 

np1 = np.array([0,1,2,3,4,5])
#create a view 
np2 = np1.view()
print(f"Original NP1 : {np1}")
print(f"Original NP2 : {np2}")
np1[0] = 41  
np2[4] = 456
print(f"Changed NP1 : {np1}")
print(f"Changed NP2 : {np2}") 
print("---------------------------------------------------------")
#create a copy 
np3 = np.array([0,1,2,3,4,5]) 
np4 = np3.copy()
print(f"Original NP3 : {np3}")
print(f"Original NP4 : {np4}")
np3[0] , np3[3] = 41 , 56 
print(f"Changed NP3 : {np3}")
print(f"Changed NP4 : {np4}") 
