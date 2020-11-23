'''
O(n²)
1. 주어진 데이터 중 최소값 찾기
2. 최소값을 맨 앞의 값과 스왑
3. 그 다음위치부터 반복
'''

import random

def sort_selection(sortList):
    size = len(sortList)
    minIndex = 0
    for i in range(0, size):
        minIndex = i
        for j in range(i+1, size):
            if sortList[minIndex] > sortList[j]:
                minIndex = j
        sortList[i], sortList[minIndex] = sortList[minIndex], sortList[i]
        print(sortList)



## Main
sortList = []
for num in range(20):
    sortList.append(random.randint(1, 1000))
print(sortList)

sort_selection(sortList)

print(sortList)

for i in range(len(sortList)):
    if i+1 < len(sortList):
        if sortList[i] > sortList[i+1]:
            print("뭔가 이상한데 {0}번째, {1}".format(i, sortList[i]))