import random

#n1 = int(random.random() * 100) + 1
#n2 = int(random.random() * 100) + 1
#if n1>n2 :
#  print(f"El numero {n1} es mayor que {n2}")
#else :
#  print(f"El numero {n1} es menor que {n2}")

numberList = []
i = 0
while i < 100:
    numberList.append(int(random.random() * 100) + 1)
    i+=1

biggestOne=0

for value in numberList:
    if value > biggestOne:
        biggestOne = value

closestOne = 0
difference = 50
valueToFind = int(random.random() * 100) + 1
for value in numberList:
    res = abs(value - 50)
    if difference > res :
        difference = res
        closestOne = value

print(f"The biggest number is {biggestOne}")
print(f"The closset number is {closestOne}")