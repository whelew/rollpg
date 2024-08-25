# **RollPG - A Command Line Role Playing Game**

A Python terminal based Role Playing Game (RPG).

# Table of Contents

## [How to Play](#how-to-play-1)

## [Objective](#objective-1)

- [Key Features](#key-features)

## [Design](#design-1)

### [Flow Chart](#flow-chart-1)

### [Import List](#imports)

- [OS](#os)
- [Random](#random)

### [Custom Modules Imports](#custom-modules-imports-1)

- [Monster](#monster)
- [Item](#item)
- [Item, Inventory, Weapon](#Item-Inventory-Weapon)
- [Event](#event)

### [Combat](#the-combat-system)

## [Future Features](#future-features-1)

- [Interactive Inventory](#interactive-inventory)
- [Armour](#armour)
- [Video Game](#video-game)

## [Testing](#testing-1)

- [Bugs and Debugging](#bugs-and-debugging)
- [PEP8 Validaiton](#pep8---validator)

## [Deployment](#deployment-1)

- [Deploying to Heroku](#deploying-to-heroku)
- [Cloning](#cloning)

## [Technologies](#technologies-1)

## [Credits](#credits-1)

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

#### Flow Chart

A mock up flow chart of how my game will run. 

- The game runs linear however using a series of user decisions the game will return a result depending on decision.
- Using import random creates random processes and will increase replay ability.
- There is one element missing on the flow chart, the combat system, whenever combat occurs because of a result of user decision, the user might die. 
- Whenever the user dies because of combat, the game will use the exit() function and be terminated. 

![Image of my Flow Chart](/assets/images/flow-chart.png)

#### Imports

A list of the imports I used for my python script.

##### **OS**

This handles system-level operations. The main purpose of importing os was for the os.system("clear") function. Because this game is a text based RPG there is a lot of text to print. This would quickly make the command line very messy. Therefore using system("clear") I would be able to clear the previous message and insert the next step of the game. This worked very effectivly for the combat, the combat system prints out your health and attack everytime, by clearing the previous message it now looks like the health is being updated as you fight the enemy.

However this did cause some issues, as I had to look back through all my functions and make sure when a function without an input is run, because it will lead onto the next function instantly. I had to make sure the text that was meant to print was not instantly getting cleared. There are still a couple of instances where this occuring so I will aim to fix this quickly.

##### **Random**

I used random specifically for its randInt function which would let me generate a random integer from 1 to n. n being any number I wish. 

Three main uses for random:

1. Random event generating, when the user selects a choice in the game. Depending on the scenario, randInt would select one option of three. For example, It might be the case nothing happens, an enemy attacks you or you find a special item.
2. The combat system, using the Hero and Monster class attack attribute, I could put the attack attribute value into the randInt(1, n) function. For example, damage = randInt(1, hero.attack). This would allow the damage to be randomly rolled between 1 and the users attack value. This worked well as when the user aquired a new weapon that would change the users attack value, the variable included in damage = randInt(1, hero.attack) would automatically know to use the new value.
3. Using random.choice to select a specific function inside the event module which I will describe below.

#### Custom Modules Imports

A lot of the features I wanted to include the game would have taken up a lot of space in the run.py file, therefore creating new custom modules I could then import into the run.py file seemed more appropriate. This did cause a few scope issues that is why the invetory is called globally so it can be accessed at any point during the game.

##### **Monster**

- Creates an Instance of Monster with the attributes(name, hp, attack)
- Includes a random_encounter function that uses randInt to select from a list of 10 different instances of Monster.
- Future Implementation, use random.choice on 3 seperate lists.

1. List of Names
2. List of integers for health
3. List of integers for attack

- Add these new values to one instance of Monster and return this instead. It would be a lot cleaner to read if done this way and also increases randomness, you would have one instance of goblin that would be very strong and another time it would be very weak.
- UPDATED: encounter_monster function now uses random.choice to select from a list of names and integers to return an instance of Monster. This has greatly reduced the length of the code and improved readability.  

##### **Item**

- Defines classes Weapon, Item and Inventory.
- Includes two seperate functions that return instances of Weapon.

The item module is where 3 main classes are created with the sole purpose of user interaction. I am able to create functions inside this module that generate instances of the classes and then return them. When called in the run.py file I am able to use their attributes to interact with the user, for example the Weapon class will then allow me to change the players current damage to the new Weapons damage.

The Item class is used to return an instance of Item which can then be added inside the users inventory, this is why when the Inventory class is called in run.py it is global, because of the scope it needed to be global to allow me to interact with it at anytime.

There is also a function inside Item that allows me to check if the player has the item in their inventory, if they do, the function will return True else it returns False. This was a useful feature to add as it allowed me to use the items in the game and manipulate the events of the game depending on what items you have aquired.

##### **Item-Inventory-Weapon**

I used from item import Item, Inventory, Weapon to allow the readability of the run.py to be cleaner. In some cases I found myself having to create an instance of these classes inside the run.py file and instead of writing item.Item(#attributes) or item.Weapon(#attributes) I was able to just write:

- Item(#attributes)
- Weapon(#attributes)

This was pruposefully to keep the code tidier for user readability.

##### **Event**

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
    return result() #The () calls the function.

### The Combat System

The combat system starts when the combat() function is called. It takes hero and enemy as arguments. The operations work as follows:

1. The enemy's name, health and attack are aquired from the Monster class, alongside the Hero health and attack being aquired from the Hero class.
2. The Hero and enemy stats are printed at the top to show the player the current health and attack power.
3. The player is then asked if they would like to (1) attack or (2) flee. During some encounters fleeing will not be an option and the player will be forced to attack.
4. Each time the player attacks, the damage will be rolled randomly between 1 and their current attack damage, the same also applies for the enemy. This gives it the D&D style game play where you would have a dice relating to your weapon, for example a d12 and you can get any number between 1 and 12.
5. After the hero attacks and the damage is calculated, the system will be cleared and printed out again.
6. A new message above will be printed first letting the player know how much damage they did and the enemy did to them followed by the stats of the hero and enemy.
7. Whenever the player drops to 0 or below a message will be printed letting the user know they have died. The game will also use the exit() to terminate the game and stop the game from continuing with future functions.
8. The same goes for the enemy, if the enemy health drops to 0 or below the combat loop will break, a message saying the enemy has died will be printed and the next function will initiate.
9. The loop will continue to run until either the user dies, the enemy dies, or in the cases where the user can flee, they flee from combat.

UPDATE: Fixed Bug. Combat now returns True if you kill the enemy or False if you decide to flee. When fleeing you were able to aquire items, now return the function returns False so it can be used in and if True else false statement to decide if you get the item.

### Future Features

#### Interactive Inventory

- Being able to interact with the inventory at any point would be very useful, having a function that would load the player stats as well as the inventory.
- This would allow me to introduce healing items, weapons suited for certain enemies, armour you can equip and change out.
- It would be a very fun feature however it would make scope a very difficult issue as well as the linear style of the game.
- I could possible make a function that is called before the main() call in which whenever the player types "Inventory" it will pause the main() function and then print out player stats and items.

#### Armour

- I would introduce a new class called Armour. This would allow the player to equip new armour they find during the game.
- The attributes would be defence and description.
- I would need to add defence as an attribute to both Hero and Monster classes, and create a function that would update the defence of the Hero class whenever the user aquired new armour, similar to the aquire_weapon function.
- The Defence would take the calculated damage integer and then subtract the defence off that integer.
- Example:

damage = randint(1, 10)
defence = hero.defence #example 2
new_damage = damage - defence # 5 - 2 = 3
return new_damage #return 3 instead of 5

#### Video Game 

- I would like to be able to turn this command line rpg into an actual video game, for example an 8 bit top down style video game like Pokemon. Where the user is able to walk around a map and interact with none player characters, go to specific locations, check their inventory whenever they would like. Have an interactive combat system where you can physically see your character make an animation. This would take a long time to code and skills I have not yet aquired. 
- I would most likely start by using [PYGame](https://github.com/pygame/pygame) which is a free and open-source cross platform library used in the development of multimedia applications like video games using Python.

### Testing

#### Bugs and Debugging

- During the course of development a few bugs did occur.
- Many of these have now been resolved.

**Combat Fleeing**
- The combat system that I created always gave the option of either 1 attacking the enemy or 2 fleeing the combat.
- The main issue that occured was during events where after combat had been called an instance of the Item class would be returned. However the game should only let you get the item by defeating the enemy. 
- I was quickly able to resolve this by adding a return True or False feature to the combat. If during combat the user would flee, the combat call would be returned as False. I was then able to use an if x is True statement to reward the user with the item else the user did not get the item.
- There was also an issue where the user could flee the cave_encounter and the final_boss encounter, during which the player should not be allowed to flee. To resolve this issue, I created if, elif, else statement targetting the Monster classes name. If the name was either, "Dragon Lord", "Dragon Paper", "Cave Monster" or "Bug Bear", the user would not be allowed to flee and forced to complete the combat, even if it resulted in death.

**The well_item Function**
- Originally this function would have a 75% chance to return an instance of weapon and a 25% chance to return None. Due to the way I set up the function call in the run.py file whenever the 25% chance of return None was called it would cause a error saying the object has no attribute called "None".
- This was a simple fix, I removed the 25% choice as the well_item function itself was a chance call anyway so what I wanted to happen was already happening in the function well_item was being called in.

**Character Name Function**
- At the beginning of the game the user is asked what they would like to call their character. 
- I immediately ran into issues as I realised the player could name themselves nothing e.g. "". They could have their name purely as numbers, or a mixture of letters and numbers. 
- I have not fully resolved this issue, I was able to somewhat damage control it by using and if "any(n.isdigit() for n in name)", "elif name.isspace() is True:", "elif name == "":" else statement.
- Using this method meant the user could not create a name using blank space, nothing at all or have any number in the name. 
- The issue is, the user could still call themselves a single letter such as L or X, and if the user wanted a name with two words such as "Super Mario" because this name has a blank space in between the two words, it would be picked up by my elif statement.
- This is a very minor issue.

**Scope**
- Scope was a difficult issue to deal with, especially when importing seperate modules that create instances of a class.
- The inventory I called globally near to the top of the run.py file as this would allow me to use it globally in my functions below. This proved to be a useful and quick fix.
- I had thought about doing the same with the Hero class and the character name. Setting up the Hero class globally would be useful because a lot of my functions use hero as an argument in the main() function, and it might get confusing if another developer was working on this game.
- It was a fun challenge working around this, for example the combat system could have been a lot easier if I set up the monster and hero class instances globally. But i was able to figure out an appropriate method that performed the way I wanted it to perform.

#### PEP8 - Validator

I used the [Code Institute Python Linter](https://pep8ci.herokuapp.com/#) to check all my py files for errors. This was useful in fixing any syntax errors such as whitespace.

- **run.py**
![PEP8 validation image of .py](/assets/images/pep8-runpy.png)

- **item.py**
![PEP8 validation image of .py](/assets/images/pep8-item.png)

- **event.py**
![PEP8 validation image of .py](/assets/images/pep8-event.png)

- **monster.py**
![PEP8 validation image of .py](/assets/images/pep8-monster.png)

### Deployment

To be able to share my working project for the assessment, I used the Code Institute python template which included most of the files that would be needed to get it working in a mock terminal. I deployed my project to [Heroku](https://dashboard.heroku.com/).

#### Deploying to Heroku

Before deploying you need to ensure your workspace is ready to deploy.

1. If you have any inputs please ensure that they all have a new line feature (\n) as without it there maybe issues when the project is deployed.
2. You need to create your list of requirements that our project needs to run. If you have used the Code Institute Template you will have a file titled reqiurements.txt, if you do not then please create one in your project.
3. In the command line, you must input: "pip3 freeze > requirements.txt", after doing this it will add a list of dependencies to your requirements.txt file, note: it is case sensitive so please ensure everything is spelt correctly. Make sure to commit this and push it to github.
4.  Now please follow the link above to Heroku and sign in, if you don't have an account please sign up and create one.
5. Once you have done this, on the Heroku dashboard you will need to click "Create New App", name the app an appropriate name and set it to your local region, my local region was Europe.
6. Once this is done you will need to click settings, inside settings you will need to add a new config vars (Enviroment Variables). This is where you would store sensitive data.
7. Inside Key please type "PORT" and inside Value please type "8000". You need to do this or your deployment may fail.
8. (Optional) If you have a creds.json file, you will need to do this. If you are not connecting to an API you will not need to do this. Set the Key to CREDS and inside the Value add all of your creds.json file code.
9. You now need to add your buildpacks, click the "Add Buildpack" button and add Python and nodejs. Make sure that Python is above nodejs in the list.
10. Now click the Deploy tab, for deployment method please select GitHub.
11. Search for your GitHub repository name. My repository name was rollpg, so I typed this and located my project.
12. (Optional)You can choose to enable automatic deploys, I would recommend doing this as whilst you are working on your project when you push your project it will automatically update your Heroku deployment.
13. Underneath there is a manual deploy option, click the "Deploy Brach" button, please click this so you can see the deployment logs as the app is built. Note: There was an issue with one of my dependencies that stopped my app from being deployed, seeing the logs let me see which dependencie it was and remove it.
14. Once you have clicked the "Deploy Branch" button and it has completed deploying you will have a message saying the app was deployed successfully and a button underneath that will take you to your deployed project.
15. You have now completed your deployment.  


#### Cloning

- Instructions to clone: 

1. Follow Link: https://github.com/whelew/rollpg.git.
2. Click on the green code button. 
3. Copy the HTTPS URL or Github CLI link. 
4. Open Git Bash. 
5. Change your current working directory to the location where you want the clone directory.
6. Type git clone, followed by the URL you copied. 
7. Press enter to create your local clone.

### Technologies

- [GitHub](https://github.com/) was used for my repository location. I regularly committed and pushed my project changes to GitHub throughout the development.
- [Visual Studio Code](https://code.visualstudio.com/) was my chosen IDE. 
- [Heroku](https://dashboard.heroku.com/) was used to deploy the project.
- [Lucid](https://www.lucidchart.com/) was used to help design my flow chart.
- [w3schools](https://www.w3schools.com/) was used for trouble shooting.
- [Code Institute](https://learn.codeinstitute.net/) was a main source for information when trouble shooting and deploying my project.
- [Stack Overflow](https://stackoverflow.com/) was also used for trouble shooting.
- [Slack](https://app.slack.com/) was a helpful place to find like minded people, a useful community when trouble shooting.
- Everything was built using Python.
- Specific import libraries used were **os** and **random**.

### Credits

- Special thanks to the student care team for helping me adjust my schedule.
- Special thanks to my mentor Luke who has helped provide useful information and feedback. 
