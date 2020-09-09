# import module

# module.price(3)
# module.price_morning(4)
# module.price_soldier(5)

'''
import module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''

''' 
from module import *
price(3)
price_morning(4)
price_soldier(5)
'''

'''
from module import price, price_morning#, price_soldier
price(3)
price_morning(4)
# price_soldier(5)  Can not use 
'''
from travel import *

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# https://docs.python.org/ko/3/py-modindex.html
# 여기가면 임포트할수있는 외장함수에 대한 내용이 있음.