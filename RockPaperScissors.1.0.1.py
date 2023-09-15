# v1.0.1 moved player choice validation into function. Moved play_round into its own function. This results in more lines of code, but less redundancy.
# Future Features: 
### Allow user to set best of X instead of defaulting to three rounds
### Create a basic GUI that allows a user to push a button or image for their choice.
# Exercise from https://www.practicepython.org/
# Styleguide reference: https://peps.python.org/pep-0008/

import random 
import time #used strictly for creating delay in print statements below

print("Welcome to Rock, Paper, Scissors Classic! Compete against the computer in a best of 3 and win fabulous prizes!")
player_name = input("What is your name? ")
play_condition = input("Welcome {}. Type 'exit' to exit the game or hit enter to play a round. \n".format(player_name))
rps_choices = ["rock", "paper", "scissors"]


#player input validation
def get_player_choice():
	while True:
		playerChoice = input("{}: Select 'rock', 'paper', or 'scissors' > ".format(player_name)).lower()
		if playerChoice in {'rock', 'paper', 'scissors'}:
			return playerChoice
		else:
			print("That is not a valid choice. \n")

#compare player and comp choices. return True if player beats comp.
def compare(player_choice, comp_choice):
	compare_result = {("rock", "paper") : False,
			   ("rock", "scissors") : True,
			   ("paper", "scissors") : False,
			   ("paper", "rock") : True,
			   ("scissors", "rock") : False,
			   ("scissors", "paper") : True}
	return compare_result[(player_choice,comp_choice)]

# play a single round and return the round result
def play_round(player_choice, comp_choice, game_round):
	if player_choice == comp_choice:
		round_result = "The computer threw {}. \nYou tied round {}. \n".format(comp_choice, game_round)
	elif compare(player_choice, comp_choice):
		round_result = "The computer threw {}. \nYou win round {}. \n".format(comp_choice, game_round)
	else:
		round_result = "The computer threw {}. \nYou lose round {}. \n".format(comp_choice, game_round)
	return round_result

# play a match. first to win 2 rounds wins the match
def play_match():
	game_round = 1
	player_wins = 0
	comp_wins = 0

	while player_wins < 2 and comp_wins < 2:
		player_choice = get_player_choice()
		comp_choice = rps_choices[random.randint(0,2)]

		round_result = play_round(player_choice, comp_choice, game_round)
		print(round_result)

		if "win" in round_result:
			player_wins += 1

		if "lose" in round_result:
			comp_wins += 1

		game_round += 1

	time.sleep(1) # include a short delay in output for better usability
	if player_wins >= 2:
		print("Congratulations! You won the match in {} rounds! \n".format(game_round-1))

	else:
		print("The computer won the match in {} rounds. \n".format(game_round-1))


while play_condition != "exit":
	play_match()
	play_condition = input("Do you want to play again? Type 'exit' to exit the game or hit enter to play a round. ".format(player_name))

print("Until next time! \n")