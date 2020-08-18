class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} Unit created.".format(self.name))
    def move(self, location):
        print("{0} : {1} direction Moving. [SPD {2}".format(self.name, location, self.speed))
    def damaged(self, damage):
        print(f"{self.name} : {damage} damage taken.")
        self.hp -= damage
        print(f"{self.name} : Cur Hp {self.hp}")
        if self.hp <= 0 :
            print(f"{self.name} destroyed")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, dmg):
        Unit.__init__(self, name, hp, speed)       # 부모의 생성자를 이러케 호출하믄 됨둥
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