'''
# glob : 경로 내의 폴더 / 파일 목록 조회
import glob
print(glob.glob("./Practice/*"))
'''
# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("폴더있음")
else:
    os.makedirs(folder)
    print("폴더 만듦")