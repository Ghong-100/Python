'''
치킨 자동 주문 제작 시스템.

조건1 : 1보자 작거나 숫자가 아닌 값이 들어올 때는 ValueError 처리
        출력 : 잘못된 값을 입력하였습니다.
조건2 : 준비된 닭은 총 10마리임
        치킨 소진시 SoldOut 에러 발생 후 종료
        출력 : 재고가 소진되어 더 이상 주문을 받지 않습니다.
'''

chicken = 10
waiting = 1 # 대기번호 1부터 시작

class SoldOut(Exception):
    def __str__(self):
        return "재고가 소진되어 더 이상 주문을 받지 않습니다."

while(True):
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("주문 수량 : "))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문 완료".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOut
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOut as err:
        print(err)
        break



