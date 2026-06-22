import numpy as np 

# create 1-D Numpy Array and get shape 
np1= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print (np1)
print (np1.shape)

# create 2-D Array and get shape (rows/columns )
np2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(np2 )
print(np2.shape)
np3 = np.array([[1,2,3 ,4] ,[5,6,7,8], [9,10,11,12]])
print(np3 )
print(np3.shape)
np4 = np1.reshape(3,4)
print(np4)
print(np4.shape)
# Reshape 3-D
np5 = np1.reshape(2,3,2)
print(np5)
print(np5.shape)
# Flatten to 1-D  
np6 = np5.reshape(-1)
print(np6)
print(np6.shape)