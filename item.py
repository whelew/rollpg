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
        Item("Iron Sword", 6)
    elif h_name == "Dwarf":
        Item("Iron Axe", 5)
    elif h_name == "Elf":
        Item("Short Bow", 7)
    else:
        Item("Hands", 2)