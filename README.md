# colors
Модуль для создания своего фона, аватарки и т.д.
![Снимок экрана от 2023-06-01 14-22-07](https://github.com/bolgaro4ka/colors/assets/123888141/db574806-500c-4752-9eb4-d39f09565989)
Имеется всего одна функция backgrounds()
В неё передаются следующие параметры:

 -     mod - режим программы:
     -     random_text - один цвет фона, случайный цвет для текста, 
     -     repeat_text - один цвет фона, цвет для текста повторяется n_repeat количество раз
     -     repeat - цвет фона повторяется n_repeat количество раз,один цвет для текса,
     -     random -  случайный цвет для фона, один цвет для текста, 
     -     combi - случайный цвет для фона, случайный цвет для текста

 -     colors - какие цвета будут использованы, по умолчанию все

 -     text - текст, по умолчанию ' '

 -     sleep - определяет быстроту отображения текста (чем больше, тем медленей), по умолчанию 0.00001

 -     n_repeat - количество повторений (имеет смысл для mod = repeat_text и repeat), по умолчанию 20


ПРИМЕРЫ:
 - backgrounds(mod='random_text', text='H')
 - backgrounds(mod='combi', text='bolgaro4ka')
 - backgrounds(mod='random', text=' ')
 - backgrounds(mod='repeat', color=[WHITE, BLUE, RED], text=' ', n_repeat=30)
 - backgrounds(mod='repeat_text', color=[WHITE, BLUE, RED], text='X', n_repeat=30)

Остановка программы: ctrl + c
![Снимок экрана от 2023-06-01 15-00-25](https://github.com/bolgaro4ka/colors/assets/123888141/1e668692-a45d-4035-bb32-8e26e05c4bb3)
![Снимок экрана от 2023-06-01 15-04-28](https://github.com/bolgaro4ka/colors/assets/123888141/aaebab7b-e29c-424f-bea7-dc363a022488)
