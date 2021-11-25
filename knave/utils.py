import random
from knave.models import Name, Trait


# TODO inventory generate
class Character:
    def __init__(
            self, name: str = None, stats: dict = None, armour: int =
            None, health: int = None, traits: dict = None, inventory: list =
            None):
        self.stats = stats

        self.stats = stats
        self.stats = stats if stats is not None else self._generate_stats()
        self.name = name if name is not None else self._get_random_name()
        # 1 level characters start with from 1 to 8 hp
        self.health = health if health is not None else random.randint(1, 8)
        self.traits = traits if traits is not None else \
            self._get_random_traits()
        # Unique stat which depends on defence items

        self.armour = armour
        self.inventory = inventory if traits is not None else self._get_random_inventory()
        # TODO inventory

    def __str__(self):
        return

    def _generate_stats(self) -> dict:
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

    def _get_random_name(self) -> str:

        names = list(Name.objects.all())
        name = random.sample(names, 1)[0].name
        return name

    def _get_random_traits(self) -> dict:
        """Returns a dict with tag names as a key and its values"""
        traits = {'Body': None, 'Face': None, 'Clothing': None, 'Skin':
            None, 'Virtue': None, 'Hair': None, 'Vice': None, 'Speech':
                      None, 'Background': None, 'Misfortune': None}

        for key in traits.keys():
            raw_traits = list(Trait.objects.filter(tags__name__in=[key]))
            new_trait = random.sample(raw_traits, 1)[0].title
            traits[key] = new_trait

        return traits

    def _get_random_inventory(self) -> list:
        """Returns a list of the chracter's items from three random tables"""

        items_1 = [('Веревка', 50, 'фт'), 'Шкивы', ('Свечи', 5),
                   ('Цепь, 10', 'фт'),
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

        inventory = []

        # First table is unique, as you should obtain two random items from it
        inventory.append(random.sample(items_1, 2))
        inventory.append(random.sample(items_2, 1))
        inventory.append(random.sample(items_3, 1))

        return inventory
