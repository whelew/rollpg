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
            new_item = item.Item("Ring", "A gold ring.")
            break
        elif choice == "2":
            print("You steal the poor strangers belongings.")
            break
        elif choice == "3":
            print("You decide to put them out of their misery.")
            print("You take out your weapon and stop their sufferring.")
            print("You take a moment to make a grave for them and give them a burial")
            print("Gain 50 karma.")
            break
        else:
            print("Please enter 1, 2 or 3.")
    
    return new_item

def other_event():
    print("event 2")

def third_event():
    print("event 3")

def random_event():
    """Chooses a random event from a list of functions"""
    events = [stranger, other_event, third_event] #store function references
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