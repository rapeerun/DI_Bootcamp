import numpy as np
import pandas as pd
from numpy import random


M=np.random.randint(2,50)
N=np.random.randint(2,40)
arry_1=random.randint(100,size=(M,N))
print(arry_1)
# Print out the third row
# print(arry_1[3,:])
# # # Print out the third column
# print(arry_1[:,3])

# #  Set every element in the last row equal to 7
# arry_1[-1,:] =7
# print(arry_1)

# Set every element in the last column equal the sum of the first two columns. 

sum_1=sum(arry_1[:,0])
print(sum_1)

sum_2=sum(arry_1[:,1])
print(sum_2)

sum_3=sum_1+sum_2
print(sum_3)

arry_1[-1,:]=sum_3
print(arry_1)

