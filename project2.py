# по статистике каждый год исчезает более 580000 людей (причины исчезновения не известны).
# одной из самых распространенных причин исчезновения является "кража людей"
# Представьте, что вас похитили и вы стали жертвой.
# Какие меры вы предпримите? Сможете ли вы выбраться из страшного места?
# Попробуйте выбраться живым и невредимым!



print("""Вы проснулись в закрытом помещении и не знаеете, где именно вы находитесь. 
Перед вам находиться дверь, а рядом лестнца на первый этаж.
Что вы выберете: спуститься/ войти в комнату""")
a = str(input())
if a == "спуститься":
   print("""Вы спустились по лестнице и увидели злого пса. 
Он пристально смотрит на вас. Что вы будете делать? погладить/тихо пройти""")
   d = str(input())
   if d == "погладить":
       print("Он зарычал и бросился на вас. Что вы будте делать?"
             "убежать/не двигаться")
       f = str(input())
       if f == "убежать":
           print("Злой пес догнал вас. Вы стали его ужином.!конец!")
       else:
           print("""Вы замерли в надежде, что пес вас не заметит.
Увы, пес кинулся на вас и вы стали его ужином""")
   else:
       print("""Вы тихо прошли мимо злого пса и пошли вперед. Вы наткнулись на дверь с замком.
Что будете делать? сломать замок ногой/ вернуться назад""")
       x = str(input())
       if x == "сломать замок ногой":
           print("""Вы начали ломать замок ногой, но делали это очень громко.
Хозяин дома прибежал на шум и успел схватить вас ,
прежде чем вы успели что-то сделать. !конец!""")
else:
       print("""Вы вошли в комнату и увидели пожилого мужчину, который смотрел на стену.
Он пригласил вас пообедать. Согласиться/отказать""")
       b = str(input())
       if b == "согласиться":
           print("""Вы сели за стол, мужчина дал вам тарелку с зеленой жидкостью и заставил пить.
Пить/Не пить""")
           g = str(input())
           if g == "пить":
               print("""Вы долго смотрели на эту жидкость, но потом все равно решили выпить.
У вас помутнело в глазах. Кровь пошла из носа.
!конец!""")
           else:
               print("""Вы не решились пить зеленую жидкость, однако сумасшедший мужчина настаивал.
 Что вы будете делать? Вылить жидкость на мужчину/ опрокинуть на пол""")
               q = str(input())
               if q == "опрокинуть на пол":
                   print("""Вы опрокинули суп на пол и попытались убежать. Мужчина погнался за вами, 
но подскользнулся и упал, это дало вам время скрыться.
Вы успели выбежать во двор. Вы увидели 2 тропинки.
По какой пойдете? длинная/короткая""" )
                   l = str(input())
                   if l == "длинная":
                       print("""Вы решили пойти по длинной дороге. Это было правильное решение.
Вы смогли найти выход и вернуться к нормальной жизни
!счастливый конец!""")
                   else:
                       print("""Вы решили выбрать легкий путь.
Однако это вывело вас на более опасную тропу.
О том, Что было дальше история умалчивает...""")
               else:
                   print("""Вы попытались пролить жидкость на мужчину,
но он успел схватить вас за руку. Он вывернул вам руку и уложил на пол.
Он взял шприц и ампулу и вколол вам что-то.
вы потеряли сознание, что было дальше никому не известно.
!конец!""")
       else:
           print("""Вы отказались обедать. Это расстроило мужчину.
Он встал, направился к окну и начал кричать.
убежать/попробовать его успокоить""")
           z = str(input())
           if z == "убежать":
               print("""Вы попытались убежать, однако вы споткнулись и упали на пол.
сумасшедший мужчина схватил вас за горло и задушил. !конец!""")
           else:
               print("""Вы попытались успооить мужчину, но ничего не вышло.
Мужчина резко побежал и выпрыгнул из окна.
От шока вы упали в обморок. Все, что происходило дальше вы не знаете.
!конец!""")
