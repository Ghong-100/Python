'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "에요.")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요 ?", str(is_adult))

station = "사당"
comment = "행 열차가 들어오고 있습니다."

print(station, comment)


from random import *
print("스터디 모임 날짜는 매월 ", randrange(4, 29), "일로 선정되었습니다")

sentence = 'I am a boy'
print(sentence)
sentence2 = "Python is ez"
print(sentence2)
sentence3 = """
I am a boy.
and Python is ez
"""
print(sentence3)


jumin = "910322-1234567"
print("성별 : ", jumin[7])
print("연도 : ", jumin[0:2])
print("월   : ", jumin[2:4])
print("뒤7자리 : ", jumin[7:])
print("가능? ", jumin[:3])

print("뒤7자리(뒤에부터) : " , jumin[-7:])
# 맨 뒤에서 7번째 ~ 맨 뒤까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Py","yp"))

print("n 은 ", python.index('n'), "번째에 있음")
print("다음 n 은 ", python.index('n', python.index('n')+1), "번째에 있음")
print("n은 ", python.count('n'), "번 나옴")
print(python.find("ghong")) # find 는 없으면 -1
# print(python.index("ghong")) index는 없으면 에러남
'''

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("우와아아 %c%c%c" % ("이","야","아"))

# print("나는 {} 살 입니다.".format(20))
# print("포멧 {}고 {}네요.".format("에지","지리"))
# print("순서도 0:{0} 이렇게 1:{1} 변경가능함".format("첫번째", "두번째"))
# print("순서도 0:{1} 이렇게 1:{1} 변경가능함".format("첫번째", "두번째"))
# print("변수 {b}아도 {s}가능.".format(b="박",s="쌉")) 
# print("한글변수 {박}아도 {쌉}가능.".format(박="박",쌉="쌉")) 
# 진짜="ㄹㅇ"
# 대단하네="쩐다"
# print(f"파이썬 {진짜} {대단하네}") # f 로 적으면 변수 땡겨와서 출력 가능함

# print("별찍기\n*\n**\n***\n**\n*\n")
# print("\"큰따 '안에' 작따\"")
# print('\'짝따 "안에" 큰따\'')
# print("\"큰따 \"안에\" 큰따\"")
# print("경로 출려크 \"D:\\01_DOCUMENTS\\10_업무보고\"")
# print("커서 새치기 ㄱㄱ \r1빠!")
# print("가산디\b지털단\b지")
# print("탭\t탭탭\t\t탭래래래랱탭\t\t\t\t\t\t.")

# site = "http://naver.com"
# site2 = site.replace("http://","")
# site3 = site2[:site2.index('.')]
# site4 = site3[:3] + str(len(site3)) + str(site3.count('e')) + '!'
# print(f"{site}의 비번은 {site4} 입니둥.")

## 