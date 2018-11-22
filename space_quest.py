#Program name: space_quest.py
#An advanced classic text adventure game

import sys
import time


def lose(reason):
    print(reason, "YOU LOSE!")
    sys.exit()


def win(reason):
    print(reason, "YOU WIN!")
    sys.exit()


def bridge():
    print("You enter the bridge. The crew is dead.")
    print("The alien murderer points its ray gun at you.")
    print()
    print("Do you flee or fight? (Type 'flee' or 'fight').")

    while True:
        action = input("> ").lower()
        if "flee" in action:
            print("That was cowardly. Start again.")
            play()
        elif "fight" in action:
            lose("You are brave and honorable. And you are vaporized.")
        else:
            print("That won't help. You must flee or fight.")


def lab():
    print("You are in the science lab.")
    print("An alien larva guards the only escape.")
    print()
    print("On a table lie three weapons: a laser, a deflector, and a rock.")
    print("Choose a weapon. (Type 'laser', 'deflector', or 'rock').")

    while True:
        weapon = input("> ").lower()
        if weapon == "laser":
            lose("The alien scoffs and lays an egg in your body.")
        elif weapon == "rock":
            print("You hit the alien in the eye and it faints." )
            engineering()
        elif weapon == "deflector":
            print("Good defensive choice, but choose an offensive weapon.")
            print("Type 'laser' or 'rock'.")

            weapon = input("> ").lower()

            if weapon == "laser":
                lose("The alien scoffs and swallows you whole.")
            elif weapon == "rock":
                print("You hit the alien in its eye and it faints.")
                engineering()
            else:
                print("No such weapon exists. Try again.")
        else:
            print("No such weapon exists. Try again.")


def engineering():
    oxygen = 3
    print("You enter the engineering deck.")
    print("Three escape pods remain intact!")
    print("But the alien queens hides in one.")
    print()
    print("Which pod do you choose: pod 1, 2, or 3 (type '1', '2', or '3')")
    while True:
        try:
            pod = int(input("> "))
        except ValueError:
            print("That's not a valid number. Start over.")
            engineering()
        if pod <= 0:
            print("There's no such pod bay number. Try again.")
        elif pod == 1:
            lose("You enter the pod and the alien queen snacks on your brain.")
        elif pod == 2:
            win("You enter the pod and launch into space.")
        elif pod == 3:
            print("There's an oxygen leak in pod 3!")
            for i in range(0, oxygen + 1):
                print("WARNING: Oxygen level is " + str(oxygen))
                oxygen -= 1
                time.sleep(2)
            lose("No more oxygen. You suffocate and die.")
        else:
            print("That pod bay is empty. Try again.")


def play():
    oxygen = 3
    print("You wander the dark corridor of an abandoned spaceship.")
    print("You must find the escape pod before your oxygen runs out.")
    print("Your current oxygen level is " + str(oxygen) + ".")
    print()
    print("You spy a door to your left and a door to your right.")
    print("Which one do you take? (Type 'left' or 'right' to proceed.)")

    while oxygen > 0:
        door = input("> ").lower()
        if door == "left":
            lab()
        elif door == "right":
            bridge()
        else:
            oxygen -= 1
            if oxygen > 0:
                print("WARNING: Oxygen level is " + str(oxygen) + ".")
                print("You must choose 'left' or 'right'.")
            else:
                lose("WARNING: Oxygen level is 0.")


play()