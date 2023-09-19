import sys

pokemons = [pokemon.strip() for pokemon in sys.stdin]

set_pokemons = set(pokemons)

print(len(pokemons) - len(set_pokemons))

print(pokemons)