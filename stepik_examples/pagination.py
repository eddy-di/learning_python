class Pagination:
    def __init__(self, sequence: list, page_size: int):
        self.sequence = sequence
        self.size = page_size
        self.pages = self.page_updater(self.sequence, self.size)
        self.all_pages = [k for k in self.pages.keys()]
        self.current_page = 1
        self.total_pages = len(self.all_pages)

    def get_visible_items(self):
        if self.current_page in range(1, len(self.all_pages) + 1):
            return self.pages[self.current_page]
        else:
            if self.current_page <= 0:
                self.current_page = 1
            elif self.current_page > len(self.all_pages):
                self.current_page = len(self.all_pages)
            return self.pages[self.current_page]
    
    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = len(self.all_pages)
        return self
    
    def prev_page(self):
        self.current_page -= 1
        return self

    def next_page(self):
        self.current_page += 1
        return self
    
    def go_to_page(self, num: int):
        if num in range(1, len(self.all_pages) + 1):
            self.current_page = num
        else:
            if num <= 0:
                self.current_page = 1
            elif num > len(self.all_pages):
                self.current_page = len(self.all_pages)

    @ staticmethod
    def page_updater(sequence, page_size):
        pages =  {}
        temp = []
        count = 0
        for i in sequence:
            if len(temp) < page_size:
                temp.append(i)
            elif len(temp) == page_size:
                count += 1
                pages.setdefault(count, temp)
                temp = []
                temp.append(i)
        pages.setdefault(count + 1, temp)
        return pages


# tests

print()
print('TEST_1:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
print(pagination.get_visible_items())

print()
print('TEST_2:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

print()
print('TEST_3:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)

print()
print('TEST_4:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.prev_page()
print(pagination.get_visible_items())

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())

print()
print('TEST_5:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.go_to_page(-100)
print(pagination.get_visible_items())

pagination.go_to_page(100)
print(pagination.get_visible_items())

print()
print('TEST_6:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
print(pagination.get_visible_items())

print()
print('TEST_7:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

pagination.first_page()
print(pagination.get_visible_items())

print()
print('TEST_8:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)

print()
print('TEST_9:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.prev_page()
print(pagination.get_visible_items())

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())

print()
print('TEST_10:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.go_to_page(-100)
print(pagination.get_visible_items())

pagination.go_to_page(100)
print(pagination.get_visible_items())

print()
print('TEST_11:')
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)

pagination.last_page()
pagination.prev_page().prev_page()
print(pagination.get_visible_items())

print()
print('TEST_12:')
alphabet = list('abcd')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())

print()
print('TEST_13:')
alphabet = list('abcdefghijklmnopqrstuvwxyz')
pagination = Pagination(alphabet, 4)
pages = [7, 3, 6, 1, 4, 2, 5]

for page in pages:
    pagination.go_to_page(page)
    print(pagination.get_visible_items())