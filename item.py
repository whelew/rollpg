from random import randint

class Weapon:
    "Creates instance of weapon"
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def description(self):
        """Describe the weapon"""
        print(f"You have aquired a {self.name}. You now do between 1 and {self.damage} damage.\n")

class Item:
    """Creates instance of Item"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def item_info(self):
        """Describe the item"""
        return f"{self.name, self.description}"

class Inventory:
    """Creates instance of Inventory"""

    def __init__(self):
        self.items = [] #list to store unique items.

    def add_item(self, item):
        """Adds item to inventroy"""
        if item not in self.items:
            self.items.append(item)
        else:
            print(f"{item.name} is already in the inventory.")

    def remove_item(self, item_name):
        """Removes item from inventory"""
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item_name} was removed from your inventory.")
                return
        print(f"{item_name} not found in the inventory.")
    
    def display_inventory(self):
        """Displays inventory to user"""
        if not self.items:
            print("Iventory is empty")
        else:
            print("Inventory:")
            for item in self.items:
                print(f"{item.item_info()}")
  
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

