# テキストファイルの読み込み
# 問題、選択肢1、選択肢2、選択肢3(答え)をそれぞれ
# question,option1,option2,answerとしたリストに入れる。
# 問題、選択肢はそれぞれのリストの要素のインデックスに対応。
import re

source = 'C:/Users/haruk/PycharmProjects/pythonProject/python_challenge2_package/text_file/challenge2_text.txt'

with open(source, 'r', encoding="utf-8") as f:
    data = f.read()

questions = re.findall('第.*？', data)
answers = re.findall('A.*\n', data)
options1 = re.findall('B.*\n', data)
options2 = re.findall('C.*\n', data)

question = []
for sentence in questions:
    q = re.sub('第.問：', '', sentence)
    question.append(q)

answer = []
for word in answers:
    w = re.sub('A|\n', '', word)
    answer.append(w)

option1 = []
for word in options1:
    w = re.sub('B|\n', '', word)
    option1.append(w)

option2 = []
for word in options2:
    w = re.sub('C|\n', '', word)
    option2.append(w)
