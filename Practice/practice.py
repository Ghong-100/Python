'''
20명중에 랜덤 뽑기
1명은 치킨, 3명은 커피
shuffle과 sample을 활용

# 리스트 내부에서 무작위 셔플
shuffle(작성자)
print(작성자)

# 리스트 내부에서 무작위로 n개의 데이터 뽑
print(sample(작성자, 2))

출력 예제
 -- 당첨자 발표 --
 치킨 당첨자 : 1
 커피 당첨자 : [2, 3, 4]
  -- 축하합니다 --
'''
from random import *

user = list(range(1,21))
shuffle(user)
coffee = user.index(1)+1
user.remove(coffee)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : ", coffee)
print("커피 당첨자 : ", sample(user, 3))
print(" -- 축하합니다 -- ")