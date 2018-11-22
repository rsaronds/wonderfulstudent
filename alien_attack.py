#Program name: alien_attack.py
#A computer program for the game 'Alien Attack'
#The program imports the time module
import time

#Four variables are declared and set
player_1_score = 0
player_2_score = 0
alien_value = 5
aliens = 12

#The program begins
print("*** Alien Attack: Revenge of the Humans ***")

print()

player_1 = input("Input player 1 name: ")
player_2 = input("Input player 2 name: ")

print()

print("{}'s score is {}.".format(player_1, player_1_score))
print("{}'s score is {}.".format(player_2, player_2_score))
print("Aliens are worth {} points.".format(alien_value))
print("There are {} aliens.".format(aliens))

print()

print(f"{player_1} takes the controller...")
time.sleep(2)
print("corners an alien...")
time.sleep(2)
print("aims a ray gun...")
time.sleep(2)
print(f"And shoots! {player_1} killed the alien!")
time.sleep(2)

print()

aliens = aliens - 1
player_1_score = player_1_score + alien_value

print(f"{player_1}'s score is {player_1_score}.")
print(f"There are {aliens} aliens left.")

print()

print(f"It is now {player_2}'s turn.")