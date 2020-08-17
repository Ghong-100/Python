class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FyableUnit(Flyable, Unit):    # 2개 이상의 부모 클래스를 받을때는
    def __init__(self):             # 맨 앞의 애를 super가 받음
        super().__init__()

dropship = FyableUnit()