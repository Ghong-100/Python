'''
# if 조건:
#   처리
# else 조건:
#   처리

weather = input("What the weather today ? ")
if weather == "rain" or "snow":
    print("Need umbrella!")
elif weather == "dusty":
    print("Need mask!")
elif weather == "hot":
    print("Need fan!")
else:
    print("Go free!!!")


temp = int(input("temperature?? "))

if temp >= 30:
    print("hot!!!")
elif 30 > temp and temp >= 10:
    print("Goooooooooood!!!")
elif 10 > temp and temp >= 0:
    print("Cooooool!!")
else:
    print("ICE AGE!")


# for 문
#
# for 변수 in 범위:
#   처리처리
# 
# for waiting in [1,2,3,4,5]:
for waiting in range(1, 6):
    # print(f"Waiting : {waiting}")
    print("Waiting : {0}".format(waiting))

# 리스트 for문 돌리기
customer = ["IronMan", "Thor", "I AM GRUT"]
for custom in customer:
    print("Customer is {0}".format(custom))

# while문
customer = "Thor"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었슴둥. {1}번 남았음둥.".format(customer, index))
    index -= 1
    if index == 0:
        print("버ㅋ림ㅋ")

# 무한뤂으
customer = "Tony"
index = 0
while True:
    print("{0}, 커피가 준비되었슴둥. {1}회차".format(customer, index))
    index += 1
    if index == 3:
        break

person = ""

while person!=customer:
    print("커피 주인 찾아욤.", customer)
    person = input("누규? ")
    print(person)

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"{student}. 나가")
        break
    print("{0}. 출췤".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로함
student = list(range(1, 6))
print(student)
student = [ i+100 for i in student ]
print(student)

# 애들 이름 길이 뽑기
student = ["qewr", "ASD", "zxcvbnm"]
student = [ len(i) for i in student ]
print(student)

# 학생 이름을 대문자로
student = ["qewR", "ASD", "zxcvBnm"]
student = [ i.upper() for i in student ]
print(student)
'''

# 퀴즈
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
# 조건 1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수
# 조건 2: 태울 손님은 소요시간이 5 ~ 15분 사이인 승객만
# (출력)
# [o] 1번째 손님 ( 소요시간 : 15분 )
# [ ] 2번째 손님 ( 소요시간 : 25분 )
# [o] 3번째 손님 ( 소요시간 : 5분 )
# ...
# [ ] 50번째 손님 ( 소요신간 : 16분 )
# 총 탑승 승객 : 2명

# Customer = list(range(0,50))
# Customer = [ randrange(5,51)   for i in Customer ]
'''
from random import *
Customer = [ randrange(5,51)   for i in list(range(0,50)) ]
Count = 0
On = ' '

for i in range(0, 50):
    if Customer[i] >= 5 and Customer[i] <= 15:
        On = 'O'
        Count += 1
    else:
        On = ' '
    print("[{0}] {1}번째 손님\t( 소요시간 : {2}분 )".format(On, i+1, Customer[i]))
print(f"총 탑승 승객 : {Count}")


from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        cnt += 1
        print(f"[O] {i}번째 손님 ( 소요시간 : {time} )")
    else:
        print(f"[ ] {i}번째 손님 ( 소요시간 : {time} )")
print("총 탑승 승객 : ", cnt)
'''