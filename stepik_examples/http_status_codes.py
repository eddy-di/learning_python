from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value
    
    def code_class(self):
        class_rus = {
            'информация': range(100, 200),
            'успех': range(200, 300),
            'перенаправление': range(300, 400),
            'ошибка клиента': range(400, 500),
            'ошибка сервера': range(500, 600),
        }
        for k, v in class_rus.items():
            if self.value in v:
                return k
            

# tests

print('TEST_1:')
print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())

print('TEST_2:')
print(HTTPStatusCodes.CONTINUE.info())
print(HTTPStatusCodes.CONTINUE.code_class())

print('TEST_3:')
print(HTTPStatusCodes.USE_PROXY.info())
print(HTTPStatusCodes.USE_PROXY.code_class())

print('TEST_4:')
print(HTTPStatusCodes.NOT_FOUND.info())
print(HTTPStatusCodes.NOT_FOUND.code_class())

print('TEST_5:')
print(HTTPStatusCodes.BAD_GATEWAY.info())
print(HTTPStatusCodes.BAD_GATEWAY.code_class())

print('TEST_6:')
for instance in HTTPStatusCodes:
    print(f'{instance.name} -> {instance.value}')