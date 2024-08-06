# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def new_game():
    print("Welcome to RollPG.")
    print("To begin your new adventure we need a name.")
    character_name = input("What is your characters name:")
    return character_name

def main():
    character_name = new_game()
    print(character_name)

main()