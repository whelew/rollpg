# **RollPG - A Command Line Role Playing Game**

A Python terminal based Role Playing Game (RPG).

# Table of Contents


## [How to Play](#how-to-play-1)
## [Objective](#objective-1)
## [Design](#design-1)

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