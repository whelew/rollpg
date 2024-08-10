# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math
import sys, time
from random import randint

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

def slow_print(text):
    """
    Slowly prints out text. 
    """
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.06)

def new_game():
    print("Welcome to RollPG. You are about to embark on an epic quest.")
    print("Are you ready to take on the challenge?")
        
def character_name():
    """
    Set players name, checks to see if name contains an integer.
    Checks to see if input is blank or contains white space.
    Returns name if none of the above.
    """
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
    return name   

def select_race():

    while True:
        """
        Sets race to 1 of 3 options, using if elif statement to check 
        user input if the user does not input 1, 2 or 3
        the user will be told to select one from the list.
        """
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
    return race

def combat(enemy, hero):
    """
    Takes Monster and Hero class as arguments.
    While loop will repeat until hero or enemy health drop to or below 0.
    Rolls randint as damage between 1 and n_attack, subtracts this from n_health.
    """
    e_name = getattr(enemy, "name")
    h_name = getattr(hero, "name")
    e_health = getattr(enemy, "hp")
    h_health = getattr(hero, "hp")
    e_attack = getattr(enemy, "attack")
    h_attack = getattr(hero, "attack")

    while h_health > 0 or e_health > 0:
        print(f"Hero: Health:{h_health} Attack:{h_attack}")
        print(f"{e_name}: Health:{e_health} Attack:{e_attack}")
        print("1 to attack or 2 to flee")
        choice = input("enter 1 or 2:")
        if choice == "1":
            e_damage = randint(1, e_attack)
            h_damage = randint(1, h_attack)
            e_health = e_health - h_damage 
            h_health = h_health - e_damage
            print(f'The {e_name} dealt {e_damage}. You dealt {h_damage}.')
            if e_health <= 0:
                print(f"You successfully killed the {e_name}!")
                hero.hp = h_health
                break
            if h_health <= 0:
                print("You died.")
                break        
        elif choice == "2":
            print("You flee from combat")
            break
        else:
            print("You need to make a choice, 1 or 2?")
    
    return hero.stats()

def random_encounter():
    encounter = randint(1, 5)
    if encounter == 1:
        enc_mnst = Monster("Goblin", 10, 2)
    elif encounter == 2:
        enc_mnst = Monster("Wolf", 12, 2)
    elif encounter == 3:
        enc_mnst = Monster("Orge", 20, 4)
    elif encounter == 4:
        enc_mnst = Monster("Skeleton", 10, 3)
    else:
        enc_mnst = Monster("Dragon", 30, 5)
    return enc_mnst
    
def start_encounter(hero):
    level_one = random_encounter()
    print(level_one.description())
    print(level_one.stats())
    print("Will you attack yes or no?")
    reaction = input("please type y or n:\n")
    if reaction == "y":
        combat(level_one, hero)
    else:
        print("try to flee")

def main():
    new_game()
    c_name = character_name()
    print(f'Yes... {c_name}, a very heroic name!\n')
    race = select_race()
    print(f"A {getattr(race, 'name')} you say...\n")
    start_encounter(race)
    start_encounter(race)

main()