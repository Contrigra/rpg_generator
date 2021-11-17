import random
from knave.models import Name


class Character:
    def __init__(self, name: str, stats: dict = None, armour: int = None,
                 health: int = None):
        self.stats = stats if stats is not None else self._generate_stats()
        # unique stat, which is defined by armour items
        self.armour = armour
        self.name = name

        # 1 level characters start with from 1 to 8 hp
        self.health = health if health is not None else random.randint(1, 8)

    def __str__(self):
        return

    def _generate_stats(self) -> dict:
        """Returns a dict with stat names as a key and its value

        By the rules a stat equals the worst rolled dice out of 3"""
        self.stats = {'strength': None, 'dexterity': None, 'constitution':
            None,
                      'intelligence': None, 'wisdom': None, 'charisma': None}

        for key in self.stats:
            sequence = []
            for _ in range(3):
                sequence.append(random.randint(1, 6))
            self.stats[key] = min(sequence)

        return self.stats

    # TODO generate HP

    # TODO traits


def get_random_name() -> str:
    names = list(Name.objects.all())

    return random.sample(names, 1)[0].name

