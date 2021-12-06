import random
from typing import Dict, List, Tuple

from knave.models import Name, Trait
from collections import namedtuple


# TODO armor class calculations
class Character:
    def __init__(
            self, name: str = None, stats: dict = None, armor: int =
            None, health: int = None, traits: dict = None, inventory: list =
            None):

        self.stats = stats if stats is not None else self._generate_stats()
        self.name = name if name is not None else self._get_random_name()
        # 1 level characters start with from 1 to 8 hp
        self.health = health if health is not None else random.randint(1, 8)
        self.traits = traits if traits is not None else \
            self._get_random_traits()
        # Unique stat which depends on defence items

        self.armor = armor if armor is not None else self._get_random_armor()
        self.inventory = inventory if traits is not None else self._get_random_inventory()

    def __str__(self):
        return

    @staticmethod
    def _generate_stats() -> dict:
        """Returns a dict with stat names as a key and its value
        By the rules a stat equals the worst rolled 6-sided die out of 3"""

        stats = {'strength': None, 'dexterity': None, 'constitution':
            None,
                 'intelligence': None, 'wisdom': None, 'charisma': None}

        for key in stats:
            sequence = []
            for _ in range(3):
                sequence.append(random.randint(1, 6))
            stats[key] = min(sequence)

        return stats

    @staticmethod
    def _get_random_name() -> str:

        names = list(Name.objects.all())
        name = random.sample(names, 1)[0].name
        return name

    @staticmethod
    def _get_random_traits() -> dict:
        """Returns a dict with tag names as a key and its values"""
        traits = {'Body': None, 'Face': None, 'Clothing': None, 'Skin':
            None, 'Virtue': None, 'Hair': None, 'Vice': None, 'Speech':
                      None, 'Background': None, 'Misfortune': None}

        for key in traits.keys():
            raw_traits = list(Trait.objects.filter(tags__name__in=[key]))
            new_trait = random.sample(raw_traits, 1)[0].title
            traits[key] = new_trait

        return traits

    @staticmethod
    def _get_random_armor():
        """Returns a list of armor items"""
        # TODO list and calculate armor stat
        armor_items = [('No armor', 11), ('Gambeson', 12), ('Brigandine', 13),
                       ('Chain', 14)]
        helmets_and_shields = [
            (None, 0), ('Helmet', 1), ('Shield', 1), ('Helmet and Shield', 2)]

        armor_dict = {"body":
                          random.choices(armor_items, weights=[3, 11, 4, 1],
                                         k=1)[0],
                      "auxiliary_items":
                          random.choices(helmets_and_shields,
                                         weights=[13, 3, 3, 1], k=1)[0]}

        armor_dict['armor_class'] = armor_dict['body'][1] + armor_dict[
            'auxiliary_items'][1]

        return armor_dict

    @staticmethod
    def _get_random_inventory() -> list:
        """Returns a list of the chracter's items from three random tables"""

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
        inventory = [random.sample(items_1, 2), random.sample(items_2, 1),
                     random.sample(items_3, 1)]

        return inventory
