from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛 생성. [체력 {self.hp}, 속도 {self.speed}]")

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print(f"{self.name} 유닛 생성. [체력 {self.hp}, 속도 {self.speed}, 공격력{self.damage}]")

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, speed, damage):
        AttackUnit.__init__(self, name, hp, speed, damage) # 스피드 대신 dmg
        Flyable.__init__(self, speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
 
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #pass
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

# SupplyDepot = BuildingUnit("서플", 300, "9시")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "미린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩 사용. (HP 10 감소)".format(self.name))
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지않습니다.")

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
            AttackUnit.__init__(self, "탱크", 150, 20, 10)
            self.seize_mode = False
    
    def set_sieze_mode(self):
        if Tank.seize_developed == False:
            return
        else:
            if self.seize_mode == False:
                print(f"{self.name} : 시즈모드로 전환합니다.")
                self.damage *= 2
                self.seize_mode = True
            else:
                self.seize_mode = False
                self.damage /= 2

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드 해제합니다.")
        else:
            print(f"{self.name} : 클로킹 모드 설정합니다.")
        self.clocked != self.clocked

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_sieze_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 45))

game_over()

#aa = AttackUnit("ma", 50, 1, 5)

#Vulture = AttackUnit("벌쳐", 80, 10, 20)

#BattleCruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

# Vulture.move("11시")
# #BattleCruiser.fly(BattleCruiser.name, "9시")
# BattleCruiser.move("9시")



# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass
# game_start()
# game_over()