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

def main():
    character_name = new_game()
    print(f'Yes... {character_name}, a very heroic name!\n')
    race = select_race()
    print(f"A {race} you say...\n")

main()