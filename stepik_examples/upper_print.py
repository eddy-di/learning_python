import sys
import io 

# class UppercaseStream(io.TextIOBase):
    # def __init__(self, target_stream):
        # self._target_stream = target_stream
# 
    # def write(self, s):
        # self._target_stream.write(s.upper())

class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.uppercase_write
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write

    def uppercase_write(self, s):
        self.original_write(s.upper())


# tests 


print('TEST_1:')
print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')

print('TEST_2:')
with UpperPrint():
    print('Bee', 'Geek', 'Love', sep=' one ', end=' end')

print('TEST_3:')
text = '''Наверняка, почти все слышали расхожую байку, дескать, если засунуть лампочку в рот, то вынуть её оттуда можно 
будет только с непосредственной помощью медицинских работников. Мол, кусательный рефлекс, бла-бла-бла и так далее.
Ну и как в это поверить, если не попробовать?
Забейте в поисковик словосочетание «Лампочка во рту» и непременно наткнётесь на источник сего мифа: Как-то раз в Москве
проходил слет что-то типа заслуженных преподавателей, и среди их огромного количества оказалось всего три мужика. Ну,
они, естественно, решили это дело отметить. Собрались у одного из них в номере, и давай отмечать. Тут в люстре
перегорает стоваттная лампа. Они зовут ответственную за лампу бабушку, эта бабушка меняет им лампочку, а перегоревшую
оставляет на столике. Ну, преподаватели уже изрядно наотмечались, тут один, глядя на эту лампочку, просвещает
остальных, что если стоваттную лампочку засунуть в рот, то обратно её уже не вытащить. Завязывается спор.
Один из оппонентов — преподаватель физики — говорит: «Как так?! Я, кандидат наук, со всей ответственностью заявляю,
что если можно засунуть, то можно и вытащить!» и сует себе лампочку в рот, пробует высунуть, а она не высовывается.
Они её тянули-тянули, по-разному пробовали — не выходит. Ладно, решили ехать в травмпункт. Поймали такси, приехали,
ловят медсестру. «Вот, говорят, мужик с лампочкой во рту. Что делать?» Медсестра думает: «Во прикольщики!», начинает
их выгонять. Когда ей показывают потерпевшего, она в истерике бежит за доктором. Тот приходит, смотрит и бьет ребрами
ладоней по месту, в котором нижняя челюсть соединяется с черепом. У физика рот открывается еще шире, лампочка
высовывается, а мужик так и остается с открытым ртом. Хирург объясняет, что это нормально, просто мышцы были изрядно
напряжены, а теперь, наоборот, сильно расслаблены и сокращаться пока не будут, но часа через три можно уже будет
пробовать говорить. Заслуженные преподаватели благодарят врача и направляются назад в гостиницу на такси. Физик
спереди, остальные сзади. Ну, один из недоверчивых все ему не верит. «Не могу,— говорит,— понять, как так, и все тут!»
«Ну, на,— говорит ему зачинщик,— сам попробуй.» Тот пробует — не вытаскивается лампочка. Едут назад. Ловят медсестру.
Та в шоке бежит за хирургом. Успокаивают медсестру. Приходит хирург. Долго смеётся, но лампочку вытаскивает. Ловят
частника. Едут в гостиницу. Водитель спрашивает: «Что, мол, дебилов везешь?» Способный говорить отвечает: «Какие дебилы!
Это кандидаты наук и все такое, просто они лампочку в рот сунули, а вытащить не смогли». Водитель не верит, его
убеждают, он не убеждается, ему дают лампочку, он её сует в рот, она не вытаскивается. Разворачиваются, едут в
травмпункт. Ловят Медсестру. Успокаивают её и посылают за хирургом. Приходит хирург, долго матерится, проводит
процедуру излечения, разбивает лампочку о стол и говорит: «Чтоб не повторялось». Ладно, садятся снова в машину.
Благодарный водитель с открытым ртом везет их в гостиницу. Машину останавливает гаишник. Давай докапываться, в чем
дело — три имбицила и один алкаш в одной машине. Водитель жестами пытается объяснить, у него не получается. Единственный
нормальный, но изрядно подвыпивший объясняет-таки гаишнику, в чем дело. Тот молча идет в свою будку. Там гаснет свет.
Гаишник возвращается, открывает заднюю дверь и жестами просит подвинутся. Садится, изо рта торчит цоколь лампочки. Едут
в травмпункт. Ловят медсестру. С трудом доводят её до самотранспортабельного состояния. Она на неслушающихся ногах
направляется в сторону кабинета хирурга. Оттуда раздается женский вопль и грохот. Выходит хирург с неестественно
открытым и не закрывающимся ртом.'''

with UpperPrint():
    print(text)

print('TEST_4:')
names = ['Творимир Матвеев', 'Светлана Жданова', 'Агап Голубев', 'Макар Дьячков', 'Евпраксия Григорьева',
         'Доброслав Михайлов', 'Зинаида Турова', 'Лариса Сафонова', 'Раиса Моисеева', 'Фадей Герасимов',
         'Синклитикия Сергеева', 'Павел Чернов', 'Синклитикия Меркушева', 'Ксения Исакова', 'Зоя Богданова',
         'Александра Васильева', 'Макар Капустин', 'Антонин Терентьев', 'Марина Мамонтова', 'Станимир Калашников',
         'Фёкла Комарова', 'Милий Соколов', 'Кира Белозерова', 'Вениамин Фомичев', 'Максим Жуков', 'Симон Кудрявцев',
         'Вера Носова', 'Иванна Князева', 'Ювеналий Капустин', 'Юрий Кулаков', 'Татьяна Владимирова', 'Ия Дмитриева',
         'Спиридон Зыков', 'Майя Савина', 'Феврония Моисеева', 'Любовь Игнатьева', 'Кузьма Дорофеев',
         'Поликарп Панфилов', 'Парамон Силин', 'Платон Жуков']

with UpperPrint():
    print(*names, sep=' зпт ', end=' тчк')