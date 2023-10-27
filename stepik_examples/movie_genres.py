from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, name, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre: MovieGenres):
        return genre in self.genres
    
    def __str__(self):
        return f'{self.name}'

# tests

print('TEST_1:')
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie)

print('TEST_2:')
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))

print('TEST_3:')
movie = Movie('Scary movie', MovieGenres.COMEDY | MovieGenres.HORROR)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR))

print('TEST_4:')
movie = Movie('Avengers', MovieGenres.FANTASY | MovieGenres.ACTION)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.FANTASY | MovieGenres.ACTION))
print(movie)

print('TEST_5:')
movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
print(movie)