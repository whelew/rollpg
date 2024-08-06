# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def new_game():
    print("Welcome to RollPG.")
    print("To begin your new adventure we need a name.")
    character_name = input("What is your characters name:")
    return character_name

def select_race():

    while True:
        pick_race = input("Now select a race, are you a Human, Dwarf or an Elf:\n")
        race = pick_race.lower()

        if race == "dwarf":
            race = "dwarf"
            break
        elif race == "human":
            race = "human"
            break
        elif race == "elf":
            race = "elf"
            break
        else:
            print("I've not heard of that race before.. please select one from the list.\n")
            select_race()
    return race

def main():
    character_name = new_game()
    print(f'Yes... {character_name}, a very heroic name!\n')
    race = select_race()
    print(f"A {race} you say...\n")

main()