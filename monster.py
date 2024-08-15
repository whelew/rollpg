from random import randint

class Monster:
    """ Creates an instance of Monster """
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
  
    def description(self):
        """Describe the encounter"""
        return f"A wild {self.name} appears, what will you do?"

    def stats(self):
        """Set the encounter stats"""
        return f"{self.name} Health:{self.hp} Attack:{self.attack}"

def random_encounter():
    encounter = randint(1, 10)
    if encounter == 1:
        enc_mnst = Monster("Goblin", 10, 2)
    elif encounter == 2:
        enc_mnst = Monster("Wolf", 12, 2)
    elif encounter == 3:
        enc_mnst = Monster("Orge", 20, 4)
    elif encounter == 4:
        enc_mnst = Monster("Skeleton", 10, 3)
    elif encounter == 5:
        enc_mnst = Monster("BugBear", 15, 3)
    elif encounter == 6:
        enc_mnst = Monster("Centaur", 20, 3)
    elif encounter == 7:
        enc_mnst = Monster("Cockatrice", 20, 4)
    elif encounter == 8:
        enc_mnst = Monster("Imp", 5, 5)
    elif encounter == 9:
        enc_mnst = Monster("Stone Giant", 40, 4)
    else:
        enc_mnst = Monster("Dragon", 40, 5)
    return enc_mnst

def goblin_encounter():
    goblin = Monster("Goblin", 10, 2)
    return goblin

def bugbear():
    bugbear = Monster("BugBear", 15, 3)
    return bugbear