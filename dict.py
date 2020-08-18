cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print("\n없는값 접근 ㄱㄱ")
print("겟 : ", cabinet.get(5))
# print("대괄호 : ", cabinet[5]) 이건 프로그램 터짐

print("기본값 적용 : ", cabinet.get(5, "기본값아앙"))

print("사전 내부 키값 검색")
print(3 in cabinet)
print(5 in cabinet)

# 생성
newcabi = {"A1":"유재석", "B2":"김종국"}
print(newcabi["A1"])
print(newcabi)
# 삽입
newcabi["C3"] = "하하"
print(newcabi)
# 수정
newcabi["B2"] = "국종김"
print(newcabi)
# 삭제
del newcabi["B2"]
print(newcabi)

# key, value 둘다, 따로 출력
print(newcabi.items())
print(newcabi.keys())
print(newcabi.values())

# 정리
newcabi.clear()
print(newcabi)