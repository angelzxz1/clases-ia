from functions import randomValue
import numpy as np

arrList = []
i=0
while i<100:
    arrList.append([randomValue(),randomValue()])
    i+=1


X = np.array(arrList)
print(X)

