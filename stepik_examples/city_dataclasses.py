from dataclasses import dataclass

@dataclass
class City:
    name: str
    population: int
    founded: int

# tests

print()
print('TEST_1:')
city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print()
print('TEST_2:')
city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)

print()
print('TEST_3:')
city = City('Челябинск', 1189525, 1736)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print()
print('TEST_4:')
city = City('Москва', 13015126, 1147)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print()
print('TEST_5:')
city1 = City('Ростов', 1142162, 1749)
city2 = City('Владивосток', 605049, 1860)

print(city1)
print(city1.name)
print(city1.population)
print(city1.founded)

print(city2)
print(city2.name)
print(city2.population)
print(city2.founded)

print(city2 == city2)
print(city1 != city2)