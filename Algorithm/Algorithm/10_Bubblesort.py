import random

def sort_bubble(bubbleList):
    size = len(bubbleList) - 1
    for i in range(size):
        for j in range(size-i):
            if bubbleList[j] > bubbleList[j+1]:
                bubbleList[j], bubbleList[j+1] = bubbleList[j+1], bubbleList[j]
                #print(bubbleList)

def sort_bubble_cond(bubbleList):
    size = len(bubbleList) - 1
    for i in range(size):
        for j in range(size-i):
            if bubbleList[j] > bubbleList[j+1]:
                bubbleList[j], bubbleList[j+1] = bubbleList[j+1], bubbleList[j]
                #print(bubbleList)


## Main
bubbleList = []
for num in range(10):
    bubbleList.append(random.randint(1, 100))
#print(bubbleList)

sort_bubble(bubbleList)

print(bubbleList)