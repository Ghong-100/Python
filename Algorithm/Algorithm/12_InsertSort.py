'''
1. 두번째 인덱스부터 시작
2. 
'''
import random

def sort_insert(sortList):
    size = len(sortList)
    for i in range(1, size):
        minIndex = i
        for j in range(i-1,-1,-1):
            if sortList[i] < sortList[j]:
                minIndex = j
        sortList.insert(minIndex, sortList.pop(i))

## Main
sortList = []
for num in range(20):
    sortList.append(random.randint(1, 1000))
print(sortList)

sort_insert(sortList)

print(sortList)

for i in range(len(sortList)):
    if i+1 < len(sortList):
        if sortList[i] > sortList[i+1]:
            print("뭔가 이상한데 {0}번째, {1}".format(i, sortList[i]))