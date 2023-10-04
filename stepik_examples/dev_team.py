class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []


    def add_junior(self, *args):
        for el in args:
            res = el, 'junior'
            self.juniors.append(tuple(res))

    def add_senior(self, *args):
        for el in args:
            res = el, 'senior'
            self.seniors.append(tuple(res))

    def __iter__(self):
        yield from self.juniors
        yield from self.seniors

pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))