
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

# print(factorial(10))

def multiple(data):
    if data <= 1:
        return data
    else:
        return data*multiple(data-1)

import random
# 리스트가 주어졌을때, 리스트의 합을 리턴하는 함수
def sum_list(data):
    if len(data) == 1:
        return data.pop()
    else:
        return data.pop() + sum_list(data)

# data = []
# for i in range(10):
#     data.append(random.randint(1,100))
# print(data)
# print(sum_list(data))

# print(multiple(10))

def isPalindrome(data, index = 0):
    length = len(data)
    if index > length/2:
        return True
    elif data[index] == data[-(index+1)]:
        return isPalindrome(data, index+1)
    else:
        return False

# tes = 'ghonggnohg'
# print(isPalindrome(tes))


# 숫자가 주어졌을때 홀수면 3*n+1을 하고 짝수면 n/2를 해서 1이 나올때까지 결과 출력
def Test1(num):
    print(num)
    if num == 1:
        return
    if num%2 == 1:
        Test1(3*num+1)
    else:
        Test1(int(num/2))

# Test1(99999)

# 숫자가 주어졌을때 1,2,3의 합으로 나타낼 수 있는 경우의 수
# 4가 주어지면
# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+3
# 2+1+1
# 2+2
# 3+1
# 총 7가지
def Test2(num):
    if num <= 3:
        return 2**(num-1)
    else:
        return Test2(num-1) + Test2(num-2) + Test2(num-3)


print(Test2(6))