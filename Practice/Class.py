# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음.
# name = "마린"   # 유닛의 이름
# hp = 40         # 유닛의 체력
# dmg = 5         # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {dmg}\n")

# # 탱크 : 공격 유닛, 탱크. 포를 쏠수 있음. 일반모드/시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_dmg = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_dmg))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_dmg = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_dmg))

# def Attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


# Attack(name, "1시", dmg)
# Attack(tank_name, "1시", tank_dmg)
# Attack(tank2_name, "1시", tank2_dmg)

# ##### 개똥같음. 이 무슨 노가다임ㄷㄷ





# class Unit:
#     def __init__(self, name, hp, dmg):
#         self.name = name
#         self.hp = hp
#         self.dmg = dmg
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp, self.dmg))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# class Unit:
#     def __init__(self, name, hp, dmg):
#         self.name = name
#         self.hp = hp
#         self.dmg = dmg
#         print("{0} Unit created.".format(self.name))
#         print(f"HP {self.hp}, Dmg {self.dmg}")

# wraith1 = Unit("wraith", 80, 5)
# print("Unit is {0}, Dmg is {1}".format(wraith1.name, wraith1.dmg))

# # 마컨했음....
# wraith2 = Unit("Controlled wraith", 80, 5)
# wraith2.clocking = True         # 개쩌넹 걍 멤바변수 이렇게 만들수 있음.쌉오진다.

# if wraith2.clocking == True:
#     print("{0} is clocking.".format(wraith2.name))

# # 클래스 외부에서 변수 확장 가능함.


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} Unit created.".format(self.name))
    def damaged(self, damage):
        print(f"{self.name} : {damage} damage taken.")
        self.hp -= damage
        print(f"{self.name} : Cur Hp {self.hp}")
        if self.hp <= 0 :
            print(f"{self.name} destroyed")

class AttackUnit(Unit):
    def __init__(self, name, hp, dmg):
        Unit.__init__(self, name, hp)       # 부모의 생성자를 이러케 호출하믄 됨둥
        self.dmg = dmg
    def attack(self, location):
        print("{0} : {1} direction Attack. [DMG {2}]"\
                .format(self.name, location, self.dmg))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} direction Flying. [SPD {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):           # 다중 상속도 개쉬움
    def __init__(self, name, hp, dmg, flying_speed):
        AttackUnit.__init__(self, name, hp, dmg)
        Flyable.__init__(self, flying_speed)

Valkyrie = FlyableAttackUnit("Valkirie", 200, 6, 5)
Valkyrie.fly(Valkyrie.name, "East")
# Firebat1 = AttackUnit("Firebat1", 50, 16)
# Firebat1.attack("left")

# Firebat1.damaged(25)
# Firebat1.damaged(25)

