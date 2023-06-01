from colorama import Fore, Back, Style
from random import choice
import time

'''
Модуль для создания своего фона, аватарки и т.д.
Имеется всего одна функция - backgrounds()
В неё передаются следующие параметры:

 - mod - режим программы (random_text - один цвет фона, случайный цвет для текста, repeat_text - один цвет фона, цвет для текста повторяется n_repeat количество раз
repeat - цвет фона повторяется n_repeat количество раз,один цвет для текста, random -  случайный цвет для фона, один цвет для текста, combi - случайный цвет для фона, случайный цвет для текста)

 - colors - какие цвета будут использованы, по умолчанию все

 - text - текст, по умолчанию ' '

 - sleep - определяет быстроту отображения текста (чем больше, тем медленей), по умолчанию 0.00001

 - n_repeat - количество повторений (имеет смысл для mod = repeat_text и repeat), по умолчанию 20

ПРИМЕРЫ:
 backgrounds(mod='random_text', text='H')
 backgrounds(mod='combi', text='bolgaro4ka')
 backgrounds(mod='random', text=' ')
 backgrounds(mod='repeat', color=[WHITE, BLUE, RED], text=' ', n_repeat=30)
 backgrounds(mod='repeat_text', color=[WHITE, BLUE, RED], text='X', n_repeat=30)

Остановка программы: ctrl + c
'''
def backgrounds(mod='random_text', colors=['RED', 'YELLOW', 'GREEN', 'CYAN', 'BLUE', 'MAGENTA', 'BLACK', 'WHITE'], text='HELLO World', sleep=0.00001, n_repeat=20):

    try:
        if mod == 'combi':
            while True: exec('print((Fore.'+choice(colors)+" + Back." + choice(colors)+ " + "+"'"+text+"'"+"),end='')"); time.sleep(sleep)

        if mod == 'random_text':
            while True: exec('print((Fore.'+choice(colors)+" + "+"'"+text+"'"+"),end='')"); time.sleep(sleep)

        if mod == 'repeat_text':
            while True:
                for z in range(len(colors)):
                    for i in range(n_repeat): 
                        exec('print((Fore.'+ colors[z] + " + "+"'"+text+"'"+"), end='')"); time.sleep(sleep)

        if mod == 'repeat':
            while True:
                for z in range(len(colors)):
                    for i in range(n_repeat): 
                        exec('print((Back.'+ colors[z] + " + "+"'"+text+"'"+"), end='')"); time.sleep(sleep)

        if mod == 'random':
            while True: exec('print((Back.'+choice(colors)+" + "+"'"+text+"'"+"),end='')"); time.sleep(sleep)
    except KeyboardInterrupt: pass

if __name__ == "__main__":
    backgrounds('combi', text='Bolgaro4ka')

