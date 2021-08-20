# reading.py, random_num.py で作成したものを使って関数を定義
import random

from python_challenge2_package.challenge2_contents import reading
from python_challenge2_package.challenge2_contents import random_num

question = reading.question
answer = reading.answer
option1 = reading.option1
option2 = reading.option2
random_num = random_num.random_num


def start():
    print('\n\t雑学クイズ スタート！')


def main():
    i = 0
    point = 0
    while i < 10:
        j = random_num[i]
        print('問', i + 1, question[j])
        option = [answer[j], option1[j], option2[j]]
        random.shuffle(option)
        print(f'1:{option[0]}  2:{option[1]}  3:{option[2]}')
        try:
            your_answer = int(input('答え： '))
        except ValueError:
            print('正しい選択肢を選択してください。(1~3)')
        else:
            try:
                option[your_answer - 1]
            except IndexError:
                print('正しい選択肢を選択してください。(1~3)')
            else:
                if option[your_answer - 1] == answer[j]:
                    print('\t○正解！')
                    point += 1
                else:
                    print(f'\t×不正解。正解は、{answer[j]}です。')
                i += 1
    print(f'\nあなたの得点は、{point}点です！')

    if point < 5:
        print('ダメダメですね。\n出直してください。')
    elif point < 8:
        print('なかなかいいぞ！\nもっと頑張ろう！')
    elif point < 10:
        print('あとちょっと！\nいい感じ！')
    else:
        print('完璧です！すごい！\n天才です！')
