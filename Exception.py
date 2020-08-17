class Overflow(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한자리 숫자 계산기")
    num1 = int(input("첫번째 :"))
    num2 = int(input("두번째 :"))
    if num1 > 9 or num2 > 9:
        raise Overflow("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("[에러] 잘못된 값을 입력하였습니다.")
except Overflow as err:
    print("[에러] 오버플로우")
    print(err)
finally:
    print("계산기 끝났어유")

exit()


try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/nums[1]))
    #num1 = int(input("첫번째 숫자를 입력하세요 : "))
    #num2 = int(input("두번째 숫자를 입력하세요 : "))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("[에러] 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("[에러] ", err)


