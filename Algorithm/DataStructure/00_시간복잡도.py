## 속도가 중요함!!!!

# 1. 시간복잡도 : 실행 속도
# 2. 공간복잡도 : 메모리 사용량
# 요즘 메모리야 널널하니까 크게 신경 안씀.
# 계산하는 방법이나 알고가자
# 빅O : 최악의 실행시간
# O(1) < O(logn) < O(n) < O(nlogn) < O(n²) < O(2ⁿ) < O(n!)

# O(1)
# 정수의 절대값 구하기
n = 0
if n >= 0:
    print(f"{n} 는 양수임. 절대값 : {n}")
else:
    print(f"{n} 는 음수임. 절대값 : {-n}")

# O(n)
# (n번 반복돌음) * 3번 더 = 3n ==> O(n)
# 상수곱은 노상관
for num in range(3):
    for index in range(n):
        print(index)


# O(n²)
for i in range(n):
    for j in range(n):
        print(i*j)

def sum_all(n):
    total = 0
    for num in range(1, n):
        total += num
    return total