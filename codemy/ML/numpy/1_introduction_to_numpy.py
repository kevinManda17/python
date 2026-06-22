import numpy as np 

# list1 = [1,2,3,4,5,]
# print(list1)
# print(list1[0])

# Numpy - Numeric python 
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)
# step 2 
np2 =np.arange(10)
print(np2)
#step 3
np3 = np.arange(0, 10 ,2 )
print(np3)
np4 = np.zeros(10)
print(np4)

# Multidimensionnal  zeros 
np5 = np.zeros((2, 10 ))
print(np5 )
# step 6 
np6 = np.full((10), 6 )
print(np6)

# multidimensionnal full 
np7 = np.full((2,10), 6 )
print(np7 )
# convert python list to np 
my_list = [34,54,53,45,33]
np8 = np.array(my_list)
print(np8 )


