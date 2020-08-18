
'''
def open_account():
    print("새로운 계좌가 생성되었슴니다.")

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money} 입니다")
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었슴니다. 잔액은 ", balance - money, "원 입니다.")
        return balance - money
    else:
        print("돈도없는게 어디서 까불어")
        return balance
def withdraw_night(balance, money):
    commission = 100
    if balance >= (money + commission):
        print("수수료 비싸요")
        return commission, balance - money - commission
    else:
        print("돈더없는게 또 까불어")
        return commission, balance

open_account()

내돈 = int(0)
내돈 = deposit(내돈,1000)
내돈 = deposit(내돈,100)

내돈 = withdraw(int(내돈), 100)
내돈 = withdraw(int(내돈), 10)

수수료, 내돈 = withdraw_night(내돈, 50)
print(f"수수료 {수수료} 원이고, 잔액은 {내돈} 입니다.")


def profile(name, age=17, lang="한국어"):                             # 기본값
    print("이름 : {0}\t나이 : {1}\t언어 : {2}".format(name,age,lang))

profile("근홍", 30, "씨언어")
profile("유재석")

def profile(name, age, lang):
    print(name, age, lang)

profile(name="유재석", lang="자바", age=30)
profile(lang="파이썬", age=30,name="노홍철")
'''

# 가변인자
def profile(name, age, *lang):          # *변수명 : 가변인자 선언
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="\n") # end를 정의하면 마지막에 찍어주는걸 바꿀 수 있다. 기본값은 \n임
    for lan in lang:
        print(lan, end=' ')
    print(lang[0])

profile("우재석",20,"Py","Java","C","C+","C#")
profile("기맽오",25,"Kotlin","Swift")




