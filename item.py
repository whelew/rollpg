from random import randint

class Item:
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
        iron_sword = Item("Iron Sword", 5)
        return iron_sword
    elif h_name == "Dwarf":
        iron_axe = Item("Iron Axe", 4)
        return iron_axe
    elif h_name == "Elf":
        short_bow = Item("Short Bow", 6)
        return short_bow
    else:
        hands = Item("Hands", 1)
        return hands
    
def well_item():
    choice = randint(1, 3)
    if choice == 1:
        weapon = Item("Great Sword", 9)
    elif choice == 2:
        weapon = Item("Battle Axe", 8)
    else:
        weapon = Item("Great Bow", 10)
    return weapon