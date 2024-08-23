# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
from random import randint
import monster
import item
from item import Item, Inventory, Weapon
import event

class Hero:
    """Creates an instance of Hero"""
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def description(self):
        """Describes Hero"""
        return f"You are a {self.name} on a mighty quest."
    
    def stats(self):
        """Returns Hero Stats"""
        return f"{self.name} Health:{self.hp} Attack:{self.attack}"

inventory = Inventory() #Inventory instance so it can be accessed globally
        
def character_name():
    """
    Set players name, checks to see if name contains an integer.
    Checks to see if input is blank or contains white space.
    Returns name if none of the above.
    """
    print("Welcome to RollPG. You are about to embark on an epic quest.")
    print("Are you ready to take on the challenge!")
    print("To begin your new adventure we need a name.\n")
    while True:
        name = input("What is your characters name:")
        if any(n.isdigit() for n in name):
            print("You can't have a number in your name... please try again.")
        elif name.isspace() == True:
            print("You can't be called nothing...")
        elif name == "":
            print("You can't be called nothing...")
        else:
            break
    os.system("clear")
    return name   

def select_race():
    """
    Sets race to 1 of 3 options, using if elif statement to check 
    user input if the user does not input 1, 2 or 3
    the user will be told to select one from the list.
    """
    while True:
        print("Now select a race, are you a Human, Dwarf or an Elf")
        pick_race = input("Enter 1, 2, or 3:\n")
        race = pick_race

        if race == "1":
            race = Hero("Human", 50, 3)
            break
        elif race == "2":
            race = Hero("Dwarf", 60, 2)
            break
        elif race == "3":
            race = Hero("Elf", 40, 4)
            break
        else:
            print("I've not heard of that race before.. please select one from the list.\n")
    os.system("clear")        
    return race

def combat(enemy, hero):
    """
    Takes Monster and Hero class as arguments.
    While loop will repeat until hero or enemy health drop to or below 0.
    Rolls randint as damage between 1 and n_attack, subtracts this from n_health.
    """
    e_name = getattr(enemy, "name")
    e_health = getattr(enemy, "hp")
    h_health = getattr(hero, "hp")
    e_attack = getattr(enemy, "attack")
    h_attack = getattr(hero, "attack")

    print(f"You charge at the {e_name} unleashing a mighty battle chant!\n")

    while h_health > 0 or e_health > 0:
        print(f"Hero: Health:{h_health} Attack:{h_attack}")
        print(f"{e_name}: Health:{e_health} Attack:{e_attack}\n")
        print("1 to attack or 2 to flee")
        choice = input("enter 1 or 2:\n")
        if choice == "1":
            os.system("clear")
            e_damage = randint(1, e_attack)
            h_damage = randint(1, h_attack)
            e_health = e_health - h_damage 
            h_health = h_health - e_damage
            print(f'The {e_name} dealt {e_damage}. You dealt {h_damage}.\n')
            if e_health <= 0:
                os.system("clear")
                print(f"You successfully killed the {e_name}!\n")
                hero.hp = h_health
                break
            if h_health <= 0:
                os.system("clear")
                print("You died.")
                break        
        elif choice == "2":
            os.system("clear")
            print("You flee from combat")
            break
        else:
            print("You need to make a choice, 1 or 2?")
    
    return hero.stats()
    
def start_encounter(hero):
    level_one = monster.random_encounter()
    print(level_one.description())
    print(level_one.stats())
    print("Will you attack yes or no?\n")
    while True:
        reaction = input("Please type 1 for yes or 2 for no:\n")
        if reaction == "1":
            os.system("clear")
            combat(level_one, hero)
            break
        elif reaction == "2":
            os.system("clear")
            print("You flee from the encounter.")
            break
        else:
            print("Please input 1 or 2")

def cave_encounter(hero):
    level_one = monster.random_encounter()
    print(level_one.description())
    print(level_one.stats())
    print("Will you attack yes or no?\n")
    while True:
        reaction = input("Please type 1 for yes or 2 for no:\n")
        if reaction == "1":
            os.system("clear")
            combat(level_one, hero)
            break
        elif reaction == "2":
            os.system("clear")
            print("You can't escape from this encounter.")
            print("Please enter 1:")
        else:
            print("Please enter 1 or 2:")

def wishing_well(hero):
    print("You stumble upon a wishing well. Would you like to throw a coin?")
    while True:
        choice = input("Enter 1 to throw a coin, 2 to walkaway:\n")
        if choice == "1":
            chance = randint(1, 2)
            if chance == 1:
                os.system("clear")
                print("You throw the coin and hear it hit something at the bottom of the well.\n")
                new_item = item.well_item()
                acquire_weapon(hero, new_item)
                break
            else:
                os.system("clear")
                print("You throw a coin down a well.. nothing happens\n")
                break
        if choice == "2":
            os.system("clear")
            goblin = monster.goblin_encounter()
            print("You walk away and get attacked by a goblin.\n")
            combat(goblin, hero)
            break
        else:
            print("Make a choice, 1 or 2.")      

def enter_forest(hero):
    os.system("clear")
    print("You follow a stone path that leads deep into the forest.")
    choice = randint(1, 3)
    if choice == 1:
        wishing_well(hero)
    elif choice == 2:
        while True:
            print("You see a treasure chest being pulled on a cart by a Bugbear.")
            print("Would you like to attack the BugBear?")
            engage = input("Enter 1 to attack or 2 to let him pass:\n")
            if engage == "1":
                bug_bear = monster.bugbear()
                combat(bug_bear, hero)
                print("You open the chest and find.. a key.")
                key = Item("Key", "A rusty old key, I wonder what it opens...\n")
                inventory.add_item(key)
                inventory.display_inventory()
                break
            elif engage == "2":
                print("You let the BugBear pass.")
                break
            else:
                print("Please enter 1 or 2.\n")
    else:
        os.system("clear")
        print("Your journey goes smoothly and nothing out of the ordinary occurs.\n")

def forest_middle(hero):
    print("You carry on down the path. You hear a sound coming from behind a rock.")
    print("Would you like to check out the noise?")
    choice = input("1 for yes, 2 for no:\n")
    while True:
        if choice == "1":
            chance = randint(1, 2)
            if chance == 1:
                os.system("clear")
                print("You see a creature eating a human for lunch.")
                print("It sees you looking its way.\n")
                start_encounter(hero)
                print("It looks like the creaute was trying to hide an item.\n")
                map = Item("Map", "A map of the dungeon, this might come in handy...")
                inventory.add_item(map)
                inventory.display_inventory()
                break
            else:
                pass
        elif choice == "2":
            os.system("clear")
            print("You carry on walking down the path.\n")
            break
        else:
            print("Please enter 1 or 2:")

def start_quest(hero):
    print("It is time to begin your quest!\n")
    print("There has been a lot of disturbances from a nearby Dungeon in the Forest.")
    print("The Goblins and BugBears that take residence there have started to flee the cave.")
    print("They used to be no problem but something is driving them out.")
    print("Your quest is to find out what the disturbance is and make it go away.")
    print("Good luck adventurer!\n")
    while True:
        print("Head towards the Forest (1) or go to the Tavern (2)")
        choice = input("Enter 1 or 2:\n")
        if choice == "1":
            os.system("clear")
            print("You enter the Forest.\n")
            enter_forest(hero)
            break
        if choice == "2":
            os.system("clear")
            print("You enter the Tavern")
            break
        else:
            print("Please enter 1 or 2.")

def first_weapon(hero):
    """Changes Hero.attack to weapon.damage stats"""
    basic_weapon = item.basic_weapon(hero)
    basic_weapon.description()
    hero.attack = basic_weapon.damage

def acquire_weapon(hero, weapon):
    """Changes Hero.attack to weapon.damage stats"""
    weapon.description()
    hero.attack = weapon.damage

def handle_event(r_item):
    """
    Will take the random_event() function as an argument.
    If instance of item is returned from event.
    Item will be added to global inventory.
    """
    print("It seems like you're almost at the cave!")
    print("You carry on walking until..\n")
    try:
        item = event.random_event()
        if item:
            r_item.add_item(item)
            r_item.display_inventory()
        else: 
            raise ValueError("You best get back to your quest.\n")
        
    except ValueError as e:
        print(e)

def t_stone_event(hero):
    """
    Checks to see if the player has Time Stone in their inventory.
    If they do set players health to 100.
    """
    value = inventory.is_item_in_inventory("Time Stone")
    h_health = getattr(hero, "hp")
    if value == True:
        print("It looks like going through the portal has aged you.")
        print("You feel stronger, all your battle scars have healed.")
        print("You now have 100 health!")
        print("You may have lost about 10 years of your life though.\n")
        h_health = 100
        hero.hp = h_health
    else:
        pass

def check_for_map():
    """
    Checks your inventory to see if you have the Map item.
    Returns True if you do False if you don't.
    """
    print("You find yourself at the entrance of the cave.\n")
    value =inventory.is_item_in_inventory("Map")
    if value == True:
        print("You remember you have a map of the caves layout.")
        print("You take the map out and examine it.")
        print("It seems like there is a path scribbled on it.")
        print("You imagine it will take you to the source of the problem.")
        decision = True
    else:
        print("You enter the cave unsure of where to go next.")
        print("Do you want to head (1) into the darkness or (2) turn back?")
        choice = input("Enter 1 or 2:")
        while True:
            if choice == "1":
                os.system("clear")
                ("You enter the cave..\n")
                decision = False
                break
            else:
                os.system("clear")
                print("There's no point turning back.")
                print("You've come this far.")
                print("You need to finish the quest.")
                print("You enter the cave.\n")
                decision = False
                break
    return decision

def cave_system(hero):
    print("A horde of monsters are running your way.")
    print("It looks like they are running away from something.")
    print("You are able to get by for the most part unnoticed.")
    print("However a few spot you and decide to attack you.")
    print("Prepare yourself for the onslaught.")
    encounters = [cave_encounter, cave_encounter, cave_encounter]
    for encounter in encounters:
        encounter(hero)

def enter_cave(hero, map):
    """
    Takes returned value of check_for_map as an argument.
    If True skip cave system, else go into cave system.
    """
    while True:
        if map == True:
            print("Using the map you are able to navigate quickly through the cave system.\n")
            break
        else:
            print("Without knowing the cave system.")
            print("You stumble through the darkness trying your best to navigate the tunnels.\n")
            cave_system(hero)
            break

def healing_fountain(hero):
    print("Congratulations, you managed to survive the cave system!")
    print("Fortunately for you a mystical light appears ahead of you.")
    print("You head towards it, it looks like a water fountain.")
    print("There is an inscription written in the middle of the fountain.")
    print("It reads...\n")
    #\n to help readability
    print("For those kind of heart and who seek no riches.")
    print("Drink from me and you shall be restored stronger than before.")
    print("For those who have taken from the needy.")
    print("Who have sinned and given in to the greedy.")
    print("Do not take from these waters, your fate will have no reward.\n")
    #\n to help readability
    print("Do you want to drink from the fountains water?")
    value = inventory.is_item_in_inventory("Gold Ring")
    choice = input("Enter 1 or 2:\n")
    while True:
        if choice == "1":
            if value == True:
                os.system("clear")
                print("You drink from the fountains waters.")
                print("All of a sudden you start to lose your strength.")
                print("You hear a voice echo through your head...")
                print("'It seems as though you were greedy.'")
                print("'The Gold Ring you stole earlier doesn't belong to you.'")
                print("Your health has been set to 20.")
                print("Good luck.. I fear that you won't survive now.\n")
                h_health = 20
                hero.hp = h_health
                break
            else:
                os.system("clear")
                print("You drink from the fountains waters.")
                print("You hear a voice echo through your head...")
                print("'You are pure of heart, let your strength return.'")
                print("Your health has now been set too 125.")
                print("You won't be needing luck from now on!")
                h_health = 125
                hero.hp = h_health
                break
        elif choice == "2":
            os.system("clear")
            print("You decide it is best not to drink from the water.")
            print("You're almost at the source of the problem in the cave.")
            print("You delve deeper.\n")
            break
        else:
            print("Please enter 1 or 2:\n")


def main():
    c_name = character_name()
    print(f'Yes... {c_name}, a very heroic name!\n')
    hero = select_race()
    print(f"A {getattr(hero, 'name')} you say...\n")
    first_weapon(hero)
    start_quest(hero)
    forest_middle(hero)
    handle_event(inventory)
    t_stone_event(hero)
    cave = check_for_map()
    enter_cave(hero, cave)
    healing_fountain(hero)
    

main()