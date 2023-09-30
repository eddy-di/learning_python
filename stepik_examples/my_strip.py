class Strip:
    def __init__(self, chars: str) -> None:
        self.chars = chars

    def __call__(self, string: str):
        res = string.lstrip(self.chars)
        res = res.rstrip(self.chars)
        return res
    

strip = Strip('.,+-')

print(strip('     --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))

