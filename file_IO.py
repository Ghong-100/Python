# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80\n")       # 이건 자동 줄바꿈을 안해줌
# score_file.write("코딩 : 100\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline(), end="?")    # 4줄짜린데 더 호출해도 안터지네??
# print(score_file.readline(), end="?")
# score_file.close()
# score_file.close()
# score_file.close()              # 이것도 안터지네?
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     else:
#         print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # 리스트형태로 저장
# for line in lines:
#     print(line,end="")

# import pickle                          # 'b' 피클에선 바이너리로 저장함
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장해줌
# profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "rb")
# profile  = pickle.load(profile_file)    # 파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz
# 매주 1회 작성하는 보고서가 있음.
# 보고서는 아래와 같은 형태로 출력되어야 합니다.
'''
- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 
'''
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성 ㄱㄱ
# 파일명은 '1주차.txt', '2주차.txt' ... 와 같이 작성 ㄱㄱ

for file_num in range(1,3):
    with open("{0}주차.txt".format(file_num), "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - \n".format(file_num))
        report_file.write("부서 : \n이름 : \n업무 요약 : \n")
