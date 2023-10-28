from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str = field(compare=True)
    artist: str = field(compare=True)
    genre: str = field(repr=False, compare= False)
    year: int = field(repr=False, compare= True)


# tests

print()
print('TEST_1:')
print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))

print()
print('TEST_2:')
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

print()
print('TEST_3:')
musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)

try:
    musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
except:
    print('Error')

print()
print('TEST_4:')
musicalbum = MusicAlbum('Камнем по голове', 'КиШ', 'Хоррор-панк', 1996)

print(musicalbum.title)
print(musicalbum.artist)
print(musicalbum.genre)
print(musicalbum.year)

print()
print('TEST_5:')
musicalbum = MusicAlbum('Король и Шут', 'КиШ', 'Хоррор-панк', 1997)
print(musicalbum)

print()
print('TEST_6:')
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2013)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

print()
print('TEST_7:')
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Poverty', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)