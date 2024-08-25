import random
import item
import os


def stranger():
    """Find a straner, make a choice to rob him, save him or kill him."""
    print("You find an injured stranger pleading for help.")
    print("Do you (1) aid them?\n"
          "(2) steal their belongings?\n"
          "or (3) put them out of their misery?")
    while True:
        choice = input("please enter 1, 2 or 3:\n")
        if choice == "1":
            os.system("clear")
            print("You decide to help the stranger.")
            print("You are able to use some medicine on their wound.")
            print("Thank you for your help.")
            print("You see a gold ring around the neck of the stranger.")
            print("Do you demand the ring as payment?")
            print("Enter 1 for yes or 2 for no.\n")
            while True:
                sec_choice = input("Enter 1 or 2:\n")
                if sec_choice == "1":
                    os.system("clear")
                    print("Oh you want my ring? But it's all I have left!")
                    print("You demand the gold ring off the stranger!")
                    new_item = item.Item("Gold Ring", "It looks well worn.")
                    print("The stranger leaves crying.")
                    print("He will most likely die of starvation now.")
                    print("Lose 50 karma.\n")
                    return new_item
                elif sec_choice == "2":
                    os.system("clear")
                    print("I'd give you my gold ring, but it's all I have.")
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
            print("You imagine the stranger won't last long come night fall.")
            print("You hear a wolf howl in the distance...\n")
            new_item = item.Item("Gold Ring", "It looks well worn.")
            return new_item
        elif choice == "3":
            os.system("clear")
            print("You decide to put them out of their misery.")
            print("You take out your weapon and stop their sufferring.")
            print("You take a moment to make a grave and give them a burial.")
            print("Gain 50 karma.\n")
            break
        else:
            os.system("clear")
            print("What do you want to do with the helpless stranger?")
            print("Do you (1) aid them?\n"
                  "(2) steal their belongings?\n"
                  "or (3) put them out of their misery?\n")


def begger():
    """
    User selects option 1 or 2.
    If option 1.
    random.choice is used to select specific outcome.
    If option 2.
    Predefined response printed.
    Else user is prompted to input correct input.
    """
    print("You stumble across a helpless begger..")
    print('"Please Sir, Spare a coin?')
    while True:
        choice = input("Please enter 1 to spare a coin, 2 to walk by:\n")
        if choice == "1":
            os.system("clear")
            outcome = [
                ("The begger thanks you, you gain 2 charisma.\n"),
                ("The begger gives you a piece of parchment.\n"),
                ("The begger spits at you, 'a single coin.. cheapskate.'\n"),
                ("The begger transforms right in front of your eyes\n"
                 "from a decrepid old man, back to a youthful man.\n"
                 "He cries out, thankyou!\n"
                 "You have freed me from the curse that hag put on me.\n")]
            random_outcome = random.choice(outcome)
            if random_outcome == outcome[1]:
                print("Here take this. The Begger hands you a note.")
                parchment = item.Item("Parchment", "The note from the begger.")
                print(random_outcome)
                return parchment
            print(random_outcome)
            break
        elif choice == "2":
            os.system("clear")
            print("I can't believe you would walk past a dying old man.")
            print("Lose 1000 karma.")  # reference to the video game Fallout
            print("The begger curses you, you can only turn left.\n")
            break
        else:
            os.system("clear")
            print("Any spare coins adventurer?\n")


def time_loop():
    """
    User is given option 1 or 2.
    If option 1.
    Print text and return instance of item.
    If option 2.
    Print text and break while loop.
    Else user is prompted to input correct input. 
    """
    print("A portal appears in front of you.")
    print("Would you like to approach and interact with the portal?")
    while True:
        choice = input("Please enter 1 for yes, 2 for no:\n")
        if choice == "1":
            os.system("clear")
            print("You slowly approach the portal.")
            print("A hand reaches out and pulls you through it.")
            print("Everything goes black. After a few seconds..")
            print("You find yourself stood on the same spot.")
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
            os.system("clear")
            print("Would you like to approach the portal?\n")


def random_event():
    """Chooses a random event from a list of functions"""
    events = [stranger, begger, time_loop]  # store function references
    result = random.choice(events)
    return result()  # returns call of chosen event
