class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어)")


if __name__ == "__main__":
    ThailandPackage().detail()
elif __name__ == "travel.thailand":
    print("트래블")
else:
    print("엘스 {0}".format(__name__))