
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(10))

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

data = []

for i in range(10):
    data.append(random.randint(1,100))
print(data)
print(sum_list(data))

print(multiple(10))