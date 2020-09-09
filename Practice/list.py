## 파이썬 리스트
Mylist = [10, 20, 30]
print(Mylist)

print("20은 %d번째임" % (Mylist.index(20)+1))

Mylist.append(50)
print("서열 {}위, 신입이다. {}".format(Mylist.index(50), Mylist[Mylist.index(50)]) )
Mylist.insert(1, 11)
print("1등 사촌동생임. 서열 %d위 %d다" % (Mylist.index(11)+1, 11))

Mylist.pop()
print("더러워서 나간 막내", Mylist)

Mylist.append(5)
Mylist.sort()
print("굴러들어옴", Mylist)
Mylist.reverse()
print("하극상 ㄱㄱ", Mylist)

mix_list = ["이런것두", 123123, "가능함", True]
print(mix_list)

print("파이썬 코딩하기 개편하누누")
