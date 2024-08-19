import random
import item

def stranger():
    """Find a straner, make a choice to rob him, save him or kill him."""
    print("You find an injured stranger pleading for help.")
    print("Do you (1) aid them, (2) steal their belongings, or (3) put them out of their misery?")
    choice = input("please enter 1, 2 or 3:\n")
    while True:
        if choice == "1":
            print("You decide to help the stranger.")
            print("You are able to use some medicine on their wound.")
            print("They follow the path back to the town.")
            new_item = item.Item("Gold Ring", "A golden ring, it looks well worn.")
            return new_item
        elif choice == "2":
            print("You steal the poor strangers belongings.")
            print("Among his rations and belongings you find a gold ring.")
            print("You imagine the poor stranger won't last very long come night fall.")
            print("You hear a wolf howl in the distance...")
            new_item = item.Item("Gold Ring", "A golden ring, it looks well worn.")
            return new_item
        elif choice == "3":
            print("You decide to put them out of their misery.")
            print("You take out your weapon and stop their sufferring.")
            print("You take a moment to make a grave for them and give them a burial.")
            print("Gain 50 karma.")
            break
        else:
            print("Please enter 1, 2 or 3.")

def begger():
    print("You stumble across a helpless begger..")
    print('"Please Sir, Spare a coin?')
    choice = input("please enter 1 to spare a coin, 2 to walk by:")
    while True:
        if choice == "1":
            outcome = [
                ("The begger thanks you, you gain 2 charisma."), 
                ("The begger gives you a piece of parchment."),
                ("The begger spits at you, 'a single coin.. cheapskate.'"),
                ("""The begger transforms right in front of your eyes
                from a decrepid old man, back to a youthful man. He cries out, thank
                you! You have freed me from the curse that old hag put on me.""")]
            random_outcome = random.choice(outcome)
            if random_outcome == outcome[1]:
                parchment = item.Item("Parchment", "The note from the begger.")
                print(random_outcome)
                return parchment
            print(random_outcome)
            break
        elif choice == "2":
            print("I can't believe you would walk past a dying old man.")
            print("Lose 1000 karma.") #reference to the video game Fallout
            print("The begger curses you, you can only turn left.")
            break
        else:
            print("Please enter 1, 2.")



def time_loop():
    print("event 3")

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