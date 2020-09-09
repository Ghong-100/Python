import sys

'''
print("Python", "Java", sep = " and ")  # seperator 를 지정해서 ,로 붙인 문자열 사이에 넣어줄 수 있다.

print("Python", "Java", sep=',', end='??')
print("무엇이 더 재미있을까요오오오오오오오오오오ㅗ오오ㅗ")

print("Python", "Java", file=sys.stdout)    # 표준 출력으로 출력
print("Python", "Java", file=sys.stderr)    # 표준 에러로 출력
'''
# scores = {"math":0, "eng":50, "coding":100}
# for sub, score in scores.items():
#     print(sub.ljust(10), str(score).rjust(4), sep=":")          # l or r Just방향으로 8칸 정렬

'''
for num in range(5,16):
    print("대기번호 : ", str(num).zfill(4))
'''

# answer = input("아무값이나 입력하세요 : ")  # input으로 받는 값은 항상 str임
# answer = 10
# print(type(answer))
# print(f"입력하신값은 {answer}입")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을하고, 총 10자리 공간을 확보
#        ' '요기가 빈공간
print("{0: >10}".format(500))
# 앙수일 땐 + 로 표시, 음수일땐 -로 표시
#          '+'요게 부호 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸에 _로 채움
#          '<'가 왼쪽/오른쪽 정렬을 나타내는거임둥
print("{0:_<10}".format(500))
# 숫자 3자리마다 콤마 찍찍
print("{0:,}".format(100000000))
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))
# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하고, 빈자리는 ^표시로 채워주기
print("{0:^<+30,}".format(100000000))
# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.10f}".format(5/3))