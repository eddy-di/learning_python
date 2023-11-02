import re 


class DomainException(Exception):
    def __init__(self, message='Недопустимый домен, url или email') -> None:
        super().__init__(message)


class Domain:
    standart_pattern = r"^([a-zA-Z]+)\.([a-zA-Z]+)$"

    def __init__(self, domain_address):
        self.domain_address = domain_address
        self.result = re.fullmatch(self.standart_pattern, domain_address)
        if self.result:
            self.address = self.result.group()
        else:
            raise DomainException
        
    def __str__(self):
        return self.address
    
    @staticmethod
    def from_url(url_address):
        url_pattern = r'^(http\:\/\/|https\:\/\/)([a-zA-Z]+\.[a-zA-Z]+)$'
        result = re.fullmatch(url_pattern, url_address)
        if result:
            return Domain(result.group(2))
        raise DomainException

    
    @staticmethod
    def from_email(email_address):
        email_pattern = r'^([a-zA-Z]+@)([a-zA-Z]+\.[a-zA-Z]+)$'
        result = re.fullmatch(email_pattern, email_address)
        if result:
            return Domain(result.group(2))
        raise DomainException
        


#tests

print()
print('TEST_1:')
domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')
domain3 = Domain.from_email('support@pygen.ru')

print(domain1)
print(domain2)
print(domain3)

print()
print('TEST_2:')
try:
    domain1 = Domain('pygen..org')
except DomainException as e:
    print(e)

print()
print('TEST_3:')
domain1 = Domain('stepik.org')
domain2 = Domain.from_url('https://stepik.org')
domain3 = Domain.from_email('support@stepik.org')

print(domain1)
print(domain2)
print(domain3)

print()
print('TEST_4:')
domains = ['ip.ru', 'ao.org', 'npo.com', 'npo.com', 'zao.org', 'sibtred.info', 'ao.biz', 'npo.net', 'npo.net',
           'oao.net', 'zao.com', 'pahomov.org', 'bikova.ru', 'ooo.ru', 'transol.net', 'zao.com', 'rao.info', 'ooo.org',
           'krjukov.com', 'nikonova.com']

for d in domains:
    domain = Domain(d)
    print(domain)

print()
print('TEST_5:')
emails = ['maksim@hotmail.com', 'pavel@hotmail.com', 'taisija@hotmail.com', 'elizar@mail.ru',
          'olimpiada@mail.ru', 'alla@hotmail.com', 'fomichevagap@gmail.com', 'evseevagalina@rambler.ru',
          'sigizmund@hotmail.com', 'maslovepifan@hotmail.com', 'vikentivasilev@hotmail.com',
          'ermiltrofimov@hotmail.com', 'subbotinnikon@hotmail.com', 'polikarpshirjaev@yahoo.com', 'lukinjakov@mail.ru',
          'czatsev@yandex.ru', 'termakov@rambler.ru', 'valeri@yahoo.com', 'filimon@yandex.ru',
          'kkuznetsova@mail.ru']

for email in emails:
    domain = Domain.from_email(email)
    print(domain)

print()
print('TEST_6:')
urls = ['http://npo.com', 'http://zao.biz', 'http://ooo.edu', 'https://ooo.ru', 'http://prioskole.net',
        'http://ooo.com', 'http://bolshakova.biz', 'http://rao.biz', 'https://ip.biz', 'http://alekseev.ru',
        'http://ooo.ru', 'http://zao.biz', 'http://pk.biz', 'https://rao.biz', 'http://npo.org',
        'http://rao.com', 'http://rao.org', 'http://galkina.net', 'https://moskovskaja.biz', 'https://ao.ru']

for url in urls:
    domain = Domain.from_url(url)
    print(domain)

print()
print('TEST_7:')
domains = ['nikitin..biz', '.org', 'katren.', 'kubanskaja.edu.', '.', 'i.p.com', 'ooo.info+']

for d in domains:
    try:
        domain = Domain(d)
    except DomainException as e:
        print(e)

print()
print('TEST_8:')
emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
    except DomainException as e:
        print(e)

print()
print('TEST_9:')
urls = ['http://evseeva.info/', 'https:://ip.com/', 'https://www.ao.ru', 'https:///ip.ru', 'https://zao.',
        'https://.edu', 'http://oao.edu/', 'http://www.ip.com/', 'http://.org', 'http://abc.']

for url in urls:
    try:
        domain = Domain.from_url(url)
    except DomainException as e:
        print(e)

print()
print('TEST_10:')
domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты

print(type(domain1))
print(type(domain2))
print(type(domain3))