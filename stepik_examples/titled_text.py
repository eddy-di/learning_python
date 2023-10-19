class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance
    
    def __str__(self):
        return self.content
    
    def __init__(self, content, text_title) -> None:
        self.content = content
        self.text_title = text_title
    
    def title(self):
        return self.text_title
    

# tests

print('TEST_1:')
titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))

print('TEST_2:')
titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)

print('TEST_3:')
headlines = ['Как полностью изменить...', 'Где найти …', 'Быстрый способ...', 'Ошибки, которые приведут тебя к ...',
             'Как быстро...']
contents = ['Нужно всего лишь...', 'Обратитесь к нам, и мы всё расскажем', 'Для этого Вы должны', 'Не делай их',
            'Ну это вообще просто']

for heading, content in zip(headlines, contents):
    titledtext = TitledText(content, heading)
    print(titledtext.title(), titledtext)