import random
import item
import os

def stranger():
    """Find a straner, make a choice to rob him, save him or kill him."""
    print("You find an injured stranger pleading for help.")
    print("Do you (1) aid them, (2) steal their belongings, or (3) put them out of their misery?")
    while True:
        choice = input("please enter 1, 2 or 3:\n")
        if choice == "1":
            os.system("clear")
            print("You decide to help the stranger.")
            print("You are able to use some medicine on their wound.")
            print("Thank you for your help.")
            print("You see a gold ring around the neck of the stranger.")
            print("Do you demand the ring as payment for helping the stranger?")
            print("Enter 1 for yes or 2 for no.\n")
            while True:
                sec_choice = input("Enter 1 or 2:\n")
                if sec_choice == "1":
                    os.system("clear")
                    print("Oh you want my ring? But it's all I have left!")
                    print("You demand the gold ring off the stranger!")
                    new_item = item.Item("Gold Ring", "A golden ring, it looks well worn.")
                    print("The stranger follows the path back to the town crying.")
                    print("He will most likely die of starvation now with no money left.")
                    print("Lose 50 karma.\n")
                    return new_item
                elif sec_choice == "2":
                    os.system("clear")
                    print("I would give you my gold ring, but it's all I have.")
                    print("I was going to sell it when I got to town.")
                    print("Thank you for your help.")
                    print("I will pay you back when you return to town!\n")
                    break
                else:
                    os.system("clear")
                    print("Invalid Input.")
                    print("Would you like to demand the Gold Ring?")
                    print("Please enter 1 for yes or 2 for no:\n")
            break
        elif choice == "2":
            os.system("clear")
            print("You steal the poor strangers belongings.")
            print("Among his rations and belongings you find a gold ring.")
            print("You imagine the poor stranger won't last very long come night fall.")
            print("You hear a wolf howl in the distance...\n")
            new_item = item.Item("Gold Ring", "A golden ring, it looks well worn.")
            return new_item
        elif choice == "3":
            os.system("clear")
            print("You decide to put them out of their misery.")
            print("You take out your weapon and stop their sufferring.")
            print("You take a moment to make a grave for them and give them a burial.")
            print("Gain 50 karma.\n")
            break
        else:
            print("Please enter 1, 2 or 3.")

def begger():
    print("You stumble across a helpless begger..")
    print('"Please Sir, Spare a coin?')
    choice = input("please enter 1 to spare a coin, 2 to walk by:\n")
    while True:
        if choice == "1":
            os.system("clear")
            outcome = [
                ("The begger thanks you, you gain 2 charisma.\n"), 
                ("The begger gives you a piece of parchment.\n"),
                ("The begger spits at you, 'a single coin.. cheapskate.'\n"),
                ("""The begger transforms right in front of your eyes
                from a decrepid old man, back to a youthful man. He cries out, thank
                you! You have freed me from the curse that old hag put on me.\n""")]
            random_outcome = random.choice(outcome)
            if random_outcome == outcome[1]:
                parchment = item.Item("Parchment", "The note from the begger.")
                print(random_outcome)
                return parchment
            print(random_outcome)
            break
        elif choice == "2":
            os.system("clear")
            print("I can't believe you would walk past a dying old man.")
            print("Lose 1000 karma.") #reference to the video game Fallout
            print("The begger curses you, you can only turn left.\n")
            break
        else:
            print("Please enter 1, 2:\n")


def time_loop():
    print("A portal appears in front of you.")
    print("Would you like to approach and interact with the portal?")
    choice = input("please enter 1 for yes, 2 for no:\n")
    while True:
        if choice == "1":
            os.system("clear")
            print("You slowly approach the portal.")
            print("A hand reaches out and pulls you through it.")
            print("Everything goes black.")
            print("After a few seconds you find yourself stood in the same spot.")
            print("Only the portal has gone and you are holding something.\n")
            time_stone = item.Item("Time Stone", "What does it do?")
            return time_stone
        elif choice == "2":
            os.system("clear")
            print("You decide that you will leave it.")
            print("Messing around with random portals can never be good.")
            print("Right...?\n")
            break
        else:
            print("Please enter 1, 2:\n")

def random_event():
    """Chooses a random event from a list of functions"""
    events = [stranger, begger, time_loop] #store function references
    result = random.choice(events)
    return result() #returns call of chosen event

"""
choice = input("please enter 1, 2 or 3")
    while True:
        if choice == "1":
            print("Do something")
            break
        elif choice == "2":
            print("Do something else")
            break
        elif choice == "3":
            print("Do the last thing.")
            break
        else:
            print("Please enter 1, 2 or 3.")
"""