# **RollPG - A Command Line Role Playing Game**

A Python terminal based Role Playing Game (RPG).

# Table of Contents


## [How to Play](#how-to-play-1)

## [Objective](#objective-1)

- [Key Features](#key-features)

## [Design](#design-1)

### [Import List](#imports)

- [os](#os)
- [random](#random)

### [Custom Modules Imports](#custom-modules-imports-1)

- [monster](#monster)
- [item](#item)
- [Item, Inventory, Weapon](#Item-Inventory-Weapon)
- [event](#event)

### How to Play

- Throughout the game you will be asked to input data.
- You will need to type the input into the terminal and submit the data by hitting enter on your keyboard.
- You start the game by giving your character a name.
- The most common option you will be given is, enter 1 or 2:
- On some occassions you will be given 1, 2 or 3:
- If you try to input anything else other than 1, 2 or 3, the terminal will print a message asking you to enter either 1 or 2.

### Objective

The main objective of this project was to create a command line based Role Playing Game in the style of Dungeons and Dragons.

#### Key Features

- **Choice-Based Events:** Players will choose between 1 or 2 on how to react to an event. Sometimes a third option will be available.
- **Combat System:** Interactive combat system which uses two classes. The HERO and MONSTER class using class attributes, such as 'name', 'hp' and 'attack'.
- **Random Events** Using the import random to create random based events. After the user selects an option of 1 or 2. The event that follows will be chosen by using randInt(1, 3). This means that a random integer of either 1, 2 or 3 will be selected. Then by using an if, elif, else statement the corrosponding output will be chosen.
- **Inventory System** The game features an inventory system that allows players to collect specific items based on their choices. These items aren't interactive or viewable mid-game currently, but they play a crucial role in influencing future events and outcomes. Not all items can be collected in a single playthrough, encouraging replayability. While you can't check the inventory during gameplay at this time, future updates will enhance this functionality, enabling players to view and interact with their collected items.
- **Special Events** There will be unique scenarios placed throughout the game such as finding a healing fountain or a special chest, my advice is, make sure you get the Key and don't be taking Gold Rings!


### Design

#### Imports

###### os

###### random

I used random specifically for its randInt function which would let me generate a random integer from 1 to n. n being any number I wish. 

Three main uses for random:

1 Random event generating, when the user selects a choice in the game. Depending on the scenario, randInt would select one option of three. For example, It might be the case nothing happens, an enemy attacks you or you find a special item.
2 The combat system, using the Hero and Monster class attack attribute, I could put the attack attribute value into the randInt(1, n) function. For example, damage = randInt(1, hero.attack). This would allow the damage to be randomly rolled between 1 and the users attack value. This worked well as when the user aquired a new weapon that would change the users attack value, the variable included in damage = randInt(1, hero.attack) would automatically know to use the new value.
3 Using random.choice to select a specific function inside the event module which I will describe below.

#### Custom Modules Imports

A lot of the features I wanted to include the game would have taken up a lot of space in the run.py file, therefore creating new custom modules I could then import into the run.py file seemed more appropriate. This did cause a few scope issues that is why the invetory is called globally so it can be accessed at any point during the game.

###### monster

- Creates an Instance of Monster with the attributes(name, hp, attack)
- Includes a random_encounter function that uses randInt to select from a list of 10 different instances of Monster.
- Future Implementation, use random.choice on 3 seperate lists.
1 List of Names
2 List of integers for health
3 List of integers for attack
- Add these new values to one instance of Monster and return this instead. It would be a lot cleaner to read if done this way and also increases randomness, you would have one instance of goblin that would be very strong and another time it would be very weak.  

###### item

###### Item-Inventory-Weapon

###### event

The event module has currently 3 main functions defined inside of it. These act as in game events. The purpose of this module was to create a random event, which would change on each play through. This is decided by using random.choice.

A random function is selected using random.choice out of a list of function names. Once selected the result would then be returned as a function call.

Example: 
def function1():
    #Do Something

def function2():
    #Do something different

def function3():
    #Do something else

def random_event():
    result = random.choice(function1, function2, function 3)
    return result() #the () calls the function.
