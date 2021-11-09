import re

bodytype = [
    '1 Атлетичное 2 Мускулистое 3 Тучное 4 Изящное 5 Костлявое 6 Громадное 7 '
    'Долговязое 8 Накачанное 9 Грубое '
    '10 Худое 11 Короткое 12 Жилистое 13 Стройное 14 Дряблое 15 Статное 16 '
    'Коренастое 17 Миниатюрное 18 Великанье '
    '19 Гибкое 20 Закалённое']

hairstyle = [
    '1 Лысина 2 Косы 3 Короткострижены 4 Грубо обрезаны 5 Кудрявые '
    '6 Взлохмачены 7 Дреды 8 Грязные 9 Вьющиеся 10 Сальные 11 '
    'Ломкие 12 Длинные 13 Шикарные 14 Ироке 15 Блестящие 16 Хвост '
    '17 Шелковистые 18 Узел 19 Волнистые 20 Тонкие'
]


dataset = []
with open('traits.txt', mode='r', encoding='utf8') as traits:
    with open('traits_new.txt', mode='a', encoding='utf8') as new_traits:
        for line in traits:
            new_line = re.sub(r'\d*\s', '', line)
            new_traits.write(new_line+'\n')



def populate_character_data():
    ...
    # TODO command to populate sql database with initial data
