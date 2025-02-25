from random import randint
from random import choice


class Monster:
    """ Creates an instance of Monster """
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def description(self):
        """Describe the encounter"""
        return f"A wild {self.name} appears, what will you do?\n"

    def cave_desc(self):
        """Describe cave encounter"""
        return f"The {self.name} sees you as it's running, It attacks you.\n"

    def stats(self):
        """Set the encounter stats"""
        return f"{self.name} Health:{self.hp} Attack:{self.attack}"


def random_encounter():
    """
    Creates instance of Monster from a random selection of names and integers
    """
    m_name = ["Goblin", "Orge", "Skeleton", "Centaur", "Imp", "BugBear"]
    m_health = [10, 12, 15, 17, 18, 20, 25]
    m_attack = [1, 2, 3, 4, 5]

    enc_mnst = Monster(choice(m_name), choice(m_health), choice(m_attack))
    return enc_mnst


def cave_monster():
    """
    Creates instance of Monster for cave encounter.
    Uses randint to select a choice of 1, 2 or 3.
    Monster instance will be created depending on choice.
    """
    encounter = randint(1, 3)

    match encounter:
        case 1:
            enc_mnst = Monster("Cave Monster", 15, 3)
        case 2:
            enc_mnst = Monster("Cave Monster", 20, 4)
        case 3:
            enc_mnst = Monster("Cave Monster", 25, 5)

    return enc_mnst


def goblin_encounter():
    """Creates instance of Goblin"""
    goblin = Monster("Goblin", 10, 2)
    return goblin


def bugbear():
    """Creates instance of Bug Bear"""
    bugbear = Monster("Bug Bear", 15, 3)
    return bugbear


def dragon_lord():
    """Creates Instance of Dragon Lord"""
    dragon_lord = Monster("Dragon Lord", 100, 15)
    return dragon_lord


def dragon_paper():
    """Creates Instance of Dragon Lord Weakened"""
    dragon_lord = Monster("Dragon Lord", 50, 15)
    return dragon_lord
