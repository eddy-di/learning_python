from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country_code):
        translations = {
            "WINTER": {"en": "winter", "ru": "зима"},
            "SPRING": {"en": "spring", "ru": "весна"},
            "SUMMER": {"en": "summer", "ru": "лето"},
            "FALL": {"en": "fall", "ru": "осень"}
        }
        return translations[self.name][country_code]


# tests


print('TEST_1:')
print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))

print('TEST_2:')
for season in Seasons:
    print(season.text_value('en'), '->', season.text_value('ru'))

print('TEST_3:')
for season in Seasons:
    print(season.name, season.value)