from random import randint

class Weapon:
    "Creates instance of item"
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def description(self):
        """Describe the weapon"""
        print(f"You have aquired a {self.name}. You now do between 1 and {self.damage} damage.\n")

def basic_weapon(hero):
    """Gives starting race a weapon"""
    h_name = getattr(hero, "name")
    if h_name == "Human":
        iron_sword = Weapon("Iron Sword", 5)
        return iron_sword
    elif h_name == "Dwarf":
        iron_axe = Weapon("Iron Axe", 4)
        return iron_axe
    elif h_name == "Elf":
        short_bow = Weapon("Short Bow", 6)
        return short_bow
    else:
        hands = Weapon("Hands", 1)
        return hands

class Bag:
    """Creates Instance of Bag"""

    def __init__(self):
        pass
        

def well_item():
    choice = randint(1, 4)
    if choice == 1:
        weapon = Weapon("Great Sword", 9)
    elif choice == 2:
        weapon = Weapon("Battle Axe", 8)
    elif choice == 3:
        ("You found an empty bucket with a coin in it.")
    else:
        weapon = Weapon("Great Bow", 10)
    return weapon

