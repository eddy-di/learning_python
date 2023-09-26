class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self, program_name='GenerationPy', environment='release', loglevel='verbose', version='1.0.0'):
        self.program_name = program_name
        self.environment = environment
        self.loglevel = loglevel
        self.version = version


config = Config()
print(config.__dict__)
print('program_name' in config.__dict__)
print('environment' in config.__dict__)
print('loglevel' in config.__dict__)
print('version' in config.__dict__)