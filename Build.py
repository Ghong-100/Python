import os
import subprocess
import shlex

class WrongOption(Exception):
    def __init__(self, msg):
        self.msg = msg


print("\
=============================\n\
 Module Build Script\n\
=============================")

PWD = os.getcwd()
SRC_DIR = PWD + "/home/ghong/Workspace"  # 복붙할때 요기 조심!!!!

# print("{0}".format(PWD))

folders = os.listdir(SRC_DIR)
folders.sort()

print(len(folders))

for num in range(0, len(folders)):
    print(f"{num+1} : {folders[num]}")

Input = int(input("\nSelect Number : "))
Option = input("Build Option : ")
if Option == '':
    Option = 'n'


try:
    if Option != 'y' or Option == 'Y' or Option == 'S' or Option == 's' or Option == '':
        BLD_DIR = SRC_DIR + '/' + folders[Input-1]
        # print(BLD_DIR)
        os.chdir(BLD_DIR)
        subprocess.call(shlex.split(f"./Build.sh {Option}")) 
    else:
        raise WrongOption

except IndexError:
    print("[에러] 잘못된 디렉토리를 선택하였습니다.")
except WrongOption:
    print("[에러] 잘못된 옵션을 선택하였습니다.")
except Exception as err:
    print("[에러] ", err)
finally:
    print("끄으으읕!!!!!")

exit()