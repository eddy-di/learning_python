class HtmlTag:
    level = -1
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        self.__class__.level += 1
        if self.__class__.level == 0:
            print(f'<{self.tag}>')
        if self.__class__.level > 0 and not self.inline:
            print('  ' * self.__class__.level + f'<{self.tag}>')
        return self
    
    def print(self, text):
        if self.inline:
            print('  ' * self.__class__.level + f'<{self.tag}>{text}</{self.tag}>')
        else:
            print('  ' * (self.__class__.level + 1) + text)
    
    def __exit__(self, exc_value, exc_type, traceback):
        self.__class__.level -= 1
        if self.__class__.level == -1:
            print(f'</{self.tag}>')
        elif self.__class__.level >= 0 and not self.inline:
            print('  ' * (self.__class__.level + 1) + f'</{self.tag}>')

            


# tests

print('TEST_1:')
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

print('TEST_2:')
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

print('TEST_3:')
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')

print('TEST_4:')
with HtmlTag('div') as _:
    with HtmlTag('p') as paragraph:
        with HtmlTag('strong', True) as strong:
            strong.print('Notice:')
        paragraph.print('Your browser is ancient')

print('TEST_5:')
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')