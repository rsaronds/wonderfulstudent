#Program name: zombie_hunter.py
#Classic Text Adventure Style Game

print("***Zombie Hunter***")
print("")
print("You are in an abandoned warehouse with two exit doors.")
print("Which door do you choose? Type '1' or '2':")

try:
    door = input("> ")

except ValueError: #The user did not enter a number.
    print("That's not a valid number. Game over!")

if door == "1":

    print("A pack of zombies huddle in the dark. What do you do:")
    print("Run away or fight using your super karate skills?")
    print(("Type 'run' or 'fight'"))

    action = input("> ")

    if action == "run":
        print("Coward! The zombies give chase and eat your brain.")
        print("Game Over!")
    elif action == "fight":
        print("The zombie leader laughs and removes your internal organs.")
        print("Game Over!")
    else: #The user didn't enter 'run' or 'fight'
        print("It looks like '" + action + "'" + " worked! The zombies die.")
        print("You win!")

elif door == "2":

    print("Three zombies move toward you:")
    print("A zombie nurse covered in blood.")
    print("A headless zombie cop with a bad attitude.")
    print("A zombie kitten wielding a knife.")
    print("Which zombie do you take on first? Type 'nurse', 'cop', or 'kitten':")

    zombie = input("> ")

    if zombie == "nurse" or zombie =="cop":
        print("Never trust a zombie in uniform! You are so killed.")
        print("You become a zombie.")
        print("Game Over!")
    elif zombie == "kitten":
        print("The kitten was only pretending to be a zombie.")
        print("She hands you a cupcake.")
        print("You Win!")
    else: #The user didn't enter 'nurse', 'cop', or 'kitten'
        print("The zombies don't understand you choice. They hesitate.")
        print("You turn to escape.")
        print("A zombie uber runs you over.")
        print("You are killed. You become a zombie.")
        print("Game Over!")

else: #The user entered a number, but it wasn't 1 or 2.

    print("You have to type door number '1' or number '2'.")
    print("Game Over!")