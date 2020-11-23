'''
동적 계획법(Dynamic Programming)
 입력 크기가 작은 문제들을 해결한 후, 해당 부분의 해를 활용해서, 큰 부분의 문제를 해결-> 전체문제를 해결

 Memoization(메모이제이션)
  이전에 계산한 결과값을 가지고있다가 다시 필요하면 저장된 값을 가져와서 활용하는 방식


 ex) 피보나치 계산
    fn(5) = fn(4)         + fn(3)
          = fn(3) + fn(2) + fn(2) + fn(1)
          ...
    이런식으로 중복되는 계산이 나온다.
    이때 fn(2)같은 애들의 결과값을 저장해놨다가 참고하는 방식으로 진행한다.
'''

def fibo(num):
    if num == 0:
        return 0
    cache = [ 0 for index in range(num+1) ]
    cache[0] = 0
    cache[1] = 1
    
    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    
    return cache[num]

# print(fibo(13))

# n*n 사이즈의 격자가 있을때 왼쪽위에서 오른쪽 아래까지 가장 최적의 경로를 찾는 문제
# 이동은 오른쪽 or 아래로만 가능
# 각 방마다 가중치가 매겨져있다.
import random
def makePuzzle(size):
    grid = []
    for x in range(size):
        ylist = []
        for y in range(size):
            #print(f"x : {x}, y: {y}")
            ylist.append(random.randint(1,20))
            print("{0: >5}".format(ylist[y]), end='')
        print()
        grid.append(ylist)
    return grid

def puzzle(size):
    grid = makePuzzle(size)
    val = [[ 0 for x in range(size) ] for y in range(size) ]
    val[0][0] = grid[0][0]
    val[1][0] = grid[0][0] + grid[1][0]
    val[0][1] = grid[0][0] + grid[0][1]
    
    for x in range(size):
        for y in range(size):
            if x-1 < 0:
                val[x][y] = grid[x][y] + val[x][y-1]
            elif y-1 < 0:
                val[x][y] = grid[x][y] + val[x-1][y]
            else:
                val[x][y] = grid[x][y] + (val[x-1][y] if val[x-1][y] < val[x][y-1] else val[x][y-1])

    print("-----------------------------")

    for x in range(size):
        for y in range(size):
            print("{0: >6}".format(val[x][y]), end='')
        print()
    print("-----------------------------")
    printPath(size, val)

def printPath(size, val):
    curX = 0
    curY = 0

    for x in range(size):
        for y in range(size):
            if x == curX and y == curY:
                res = val[x][y]
                res = "(" + str(res) + ")"
                print("{0: >6}".format(res), end='')
                if x+1 == size:
                    curY += 1
                elif y+1 == size:
                    curX += 1
                else:
                    if val[x+1][y] < val[x][y+1]:
                        curX += 1
                    else:
                        curY += 1
            else:
                print("{0: >6}".format(val[x][y]), end='')
        print()

puzzle(12)