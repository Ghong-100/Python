'''
기준점(Pivot)을 정해서, 기준점보다 작은건 왼쪽, 큰건 오른쪽에 두고
왼쪽만 가지고 재귀호출해서 나누고, 오른쪽도 오른쪽만 가지고 재귀호출해서 나누고
'''

import random


def sort_quick(sortList):
    if len(sortList) <= 1:
        return sortList
    else:
        pivot = sortList[0]
        leftList, rightList = [], []
        for i in range(1, len(sortList)):
            if sortList[i] < pivot:
                leftList.append(sortList[i])
            else:
                rightList.append(sortList[i])
        return sort_quick(leftList) + [pivot] + sort_quick(rightList)



randlist = []
for x in range(1000):
    randlist.append(random.randint(0,100000))

print(sort_quick(randlist))