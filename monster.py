from random import randint

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
        return f"The {self.name} sees you as its running. It goes to strike you.\n"

    def stats(self):
        """Set the encounter stats"""
        return f"{self.name} Health:{self.hp} Attack:{self.attack}"

def random_encounter():
    encounter = randint(1, 10)

    match encounter:
        case 1:
            enc_mnst = Monster("Goblin", 10, 2)
        case 2:
            enc_mnst = Monster("Wolf", 12, 2)
        case 3:
            enc_mnst = Monster("Orge", 20, 4)
        case 4:
            enc_mnst = Monster("Skeleton", 10, 3)
        case 5:
            enc_mnst = Monster("BugBear", 15, 3)
        case 6:
            enc_mnst = Monster("Centaur", 20, 3)
        case 7:
            enc_mnst = Monster("Cockatrice", 20, 4)
        case 8:
            enc_mnst = Monster("Imp", 5, 5)
        case 9:
            enc_mnst = Monster("Stone Giant", 40, 4)
        case 10:
            enc_mnst = Monster("Dragon", 40, 5)
    return enc_mnst

def goblin_encounter():
    goblin = Monster("Goblin", 10, 2)
    return goblin

def bugbear():
    print("You charge at the BugBear unleashing a mighty battle chant.")
    bugbear = Monster("BugBear", 15, 3)
    return bugbear

def dragon_lord():
    dragon_lord = Monster("Dragon Lord", 100, 15)
    return dragon_lord

def dragon_paper():
    dragon_lord = Monster("Dragon Lord", 50, 15)
    return dragon_lord