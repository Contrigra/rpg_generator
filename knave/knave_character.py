import random
from dataclasses import dataclass

from knave.models import Name, Trait


@dataclass(slots=True)
class KnaveCharacter:
    name: str
    stats: dict
    armor: dict
    health: int
    traits: dict
    inventory: list


def generate_knave_character() -> KnaveCharacter:
    return KnaveCharacter(name=_generate_random_name(),
                          stats=_generate_random_stats(),
                          armor=_generate_random_armor(),
                          health=_generate_random_health(),
                          traits=_generate_random_traits(),
                          inventory=_generate_random_inventory())


def _generate_random_name() -> str:
    names = list(Name.objects.all())
    name = random.sample(names, 1)[0].name
    return name


def _generate_random_health() -> int:
    return random.randint(1, 8)


def _generate_random_stats() -> dict:
    """Returns a dict with stat names as a key and its value
    By the rules a stat equals the worst rolled 6-sided die out of 3"""

    stats = {'strength': None, 'dexterity': None, 'constitution': None,
             'intelligence': None, 'wisdom': None, 'charisma': None}

    for key in stats:
        sequence = []
        for _ in range(3):
            sequence.append(random.randint(1, 6))
        stats[key] = min(sequence)

    return stats


def _generate_random_armor() -> dict:
    """Returns a list of armor items and armor class number"""

    armor_items = [('Без доспеха', 11), ('Стёганая', 12), ('Бригантина',
                                                           13),
                   ('Кольчужная', 14)]
    helmets_and_shields = [
        (None, 0), ('Шлем', 1), ('Щит', 1), ('Шлем и щит', 2)]

    armor_dict = {"body":
                      random.choices(armor_items, weights=[3, 11, 4, 1],
                                     k=1)[0],
                  "auxiliary_items":
                      random.choices(helmets_and_shields,
                                     weights=[13, 3, 3, 1], k=1)[0]}

    armor_dict['armor_class'] = armor_dict['body'][1] + armor_dict[
        'auxiliary_items'][1]

    return armor_dict


def _generate_random_traits() -> dict:
    """Returns a dict with tag names as a key and its values"""
    traits = {'body': None, 'face': None, 'clothing': None, 'skin': None,
              'virtue': None, 'hair': None, 'vice': None, 'speech':
                  None, 'background': None, 'misfortune': None}

    for key in traits.keys():
        raw_traits = list(Trait.objects.filter(tags__slug__in=[key]))
        new_trait = random.sample(raw_traits, 1)[0].title
        traits[key] = new_trait

    return traits


def _generate_random_inventory() -> list:
    """Returns a list of a character's items from three random tables"""

    items_1 = [('Веревка', 50, 'фт'), 'Шкивы', ('Свечи', 5),
               ('Цепь', 10, 'фт'),
               ('Мел', 10),
               "Ломик", "Спички", "Крюк-кошка", "Молоток", "Фляга",
               "Фонарь",
               "Лампадное масло", "Замок", "Кандалы", "Зеркало",
               ("Шест", 10, "фт"), "Мешок", "Палатка", ("Колья", 5),
               ("Факелы", 5)
               ]
    items_2 = [('Шест', 10, "фт"), "Мешок", "Палатка", ("Колья", 5),
               ("Факелы",
                5),
               "Пила", "Ведро", "Ёжики", "Зубило", "Сверло", "Удочка",
               "Мраморные шарики", "Клей", "Кирка", "Песочные часы",
               "Сеть",
               "Клещи", "Отмычки", "Железный Футляр", "Гвозди"]
    items_3 = ["Благовония", "Губка", "Линзы", "Духи", "Горн", "Бутыль",
               "Мыло",
               "Подзорная Труба", "Смола", "Нитки",
               "Поддельные драг.камни",
               "Книга (чистая)", "Колода карт", "Набор кубиков",
               "Горшок для "
               "готовки",
               "Грим", "Свисток", "Муз.инструмент", "Перо и чернила",
               "Колокольчик"]

    # First table is unique, as you should obtain two random items from it
    inventory: list = random.sample(items_1, 2)
    inventory += random.sample(items_2, 1)
    inventory += random.sample(items_3, 1)

    return inventory
