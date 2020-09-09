'''
###########################
gun = 10

###########################
def checkpoint(soldiers):
    global gun  # 전역변수인 gun을 내가 좀 쓰고싶은데 내가 좀 쓰면 안돼냐 내가 좀 쓸수도 있는거잖아 안그래?
    gun = gun - soldiers
    print(f"local : {gun}")

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"local : {gun}")
    return gun

###########################

print(f"Total : {gun}")
checkpoint(2)
gun = checkpoint_ret(gun, 2)

print(f"Total : {gun}")
'''

'''
표준 체중 ㄱㄱ
    남 : 키 * 키 * 22
    여 : 키 * 키 * 21

    함수로 계산
    st_weight(height, gender)
    소수점 둘째자리까지 표시

    출력
    키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
def std_weight(height:float, gender):
    if gender == "남자":
        return (float)(height * height * 22)
    else:
        return (float)(height * height * 21)

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))



    