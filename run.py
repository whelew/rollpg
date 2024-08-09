# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math
import sys, time, random

def slow_print(text):
    """
    Slowly prints out text. 
    """
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.06)


def new_game():
    slow_print("Welcome to RollPG. You are about to embark on an epic quest.\n")
    slow_print("Are you ready to take on the challenge?\n")
        
def character_name():
    """
    Set players name, checks to see if name contains an integer.
    Checks to see if input is blank or contains white space.
    Returns name if none of the above.
    """
    slow_print("To begin your new adventure we need a name.")
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
            race = "human"
            break
        elif race == "2":
            race = "dwarf"
            break
        elif race == "3":
            race = "elf"
            break
        else:
            print("I've not heard of that race before.. please select one from the list.\n")
    return race

class Monster:
    """ Creates an instance of Monster """
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
  
    def description(self):
        """Describe the encounter"""
        return f"A wild {self.name} appears, what will you do?"

def random_encounter():
    encounter = randint(1, 2)
    if encounter == 1:
        enc_mnst = Monster("goblin", 10, 2)
    else:
        enc_mnst = Monster("wolf", 12, 2)
    return enc_mnst  

def main():
    new_game()
    c_name = character_name()
    slow_print(f'Yes... {c_name}, a very heroic name!\n')
    race = select_race()
    slow_print(f"A {race.capitalize()} you say...\n")

main()