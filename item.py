class Item:
    "Creates instance of item"
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def description(self):
        """Describe the weapon"""
        print(f"You have aquired a {self.name}.")
    
    def stats(self):
        """Describes the weapon stats"""
        print(f"{self.name} does a total of {self.damage} damage.")

def basic_weapon(hero):
    """Gives starting race a weapon"""
    h_name = getattr(hero, "name")
    if h_name == "Human":
        iron_sword = Item("Iron Sword", 3)
        return iron_sword
    elif h_name == "Dwarf":
        iron_axe = Item("Iron Axe", 2)
        return iron_axe
    elif h_name == "Elf":
        short_bow = Item("Short Bow", 4)
        return short_bow
    else:
        hands = Item("Hands", 1)
        return hands