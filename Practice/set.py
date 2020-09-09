# 집합 (set)
# 중복 불가, 노순서
my_set = {1,2,3,3,3}     # 나머지 3들은 무시함
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 둘 다 가능. 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합. 자바는 가능하지만 파이썬 못하는사람
print(java - python)
print(java.difference(python))

# 속)김태호 자바 손절 후 파이썬으로 환승(보
java.remove("김태호")
python.add("김태호")
print(java)
print(python)

watchtime = (hour, min, sec) = (1, 48, 46)
print(watchtime)