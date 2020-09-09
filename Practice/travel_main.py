# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *

from travel import *    # 이렇게해봤자 공개 설정을 안하면 폴더 내부에 있는 파일들의 내용을 가져오지못한다.
                        # __init__.py __all__ 에 넣으면 됨
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_two = thailand.ThailandPackage()
trip_two.detail()