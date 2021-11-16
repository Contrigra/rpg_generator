import random


class Character:
    def __init__(self, name: str, stats: dict = None, armour: int = None):
        self.stats = stats if stats is not None else self._generate_stats()
        # unique stat, which is defined by armour items
        self.armour = armour
        self.name = name

    def __str__(self):
        return

    def _generate_stats(self) -> dict:
        """Returns a dict with stat name as a key and its value

        By the rules a stat equals the worst rolled dice out of 3"""
        stats = {'strength': None, 'dexterity': None, 'constitution': None,
                 'intelligence': None, 'wisdom': None, 'charisma': None}

        for key in stats:
            sequence = []
            for _ in range(3):
                sequence.append(random.randint(1, 6))
            stats[key] = min(sequence)

        return stats
