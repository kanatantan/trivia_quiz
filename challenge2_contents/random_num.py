# random_num には、全問題数の中から
# ランダムに10個数字が選ばれ、リストにランダムに配列される。
import random

from python_challenge2_package.challenge2_contents import reading

question = reading.question     # 数字の上限として使用するため


random_num = []
while len(random_num) < 10:
    x = random.randint(0, len(question)-1)
    if not x in random_num:
        random_num.append(x)
