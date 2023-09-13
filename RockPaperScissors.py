#Exercise from https://www.practicepython.org/
#Efficient example using dictionaries and functions: https://codereview.stackexchange.com/questions/172337/rock-paper-scissors-game-in-python
#Styleguide reference: https://peps.python.org/pep-0008/

import random 
import time #used strictly for creating delay in print statements below

print("Welcome to Rock, Paper, Scissors Classic! Compete against the computer in a best of 3 and win fabulous prizes!")
player_name = input("What is your name? ")
play_condition = input("Welcome {}. Type 'exit' to exit the game or hit enter to play a round. \n".format(player_name))
rps_choices = ["rock", "paper", "scissors"]

def play_match():
	game_round = 1
	player_wins = 0
	comp_wins = 0
	while player_wins < 2:
		playerChoice = input("{}: Select 'rock', 'paper', or 'scissors' ".format(player_name))
		compChoice = rps_choices[random.randint(0,2)]

		if playerChoice == compChoice:
			print("The computer threw {}. \nYou tied round {}. \n".format(compChoice, game_round))
			game_round += 1

		elif compare(playerChoice, compChoice):
			print("The computer threw {}. \nYou win round {}. \n".format(compChoice, game_round))
			game_round += 1
			player_wins += 1

		else:
			print("The computer threw {}. \nYou lose round {}. \n".format(compChoice, game_round))
			game_round += 1
			comp_wins += 1

		if player_wins >= 2:
			time.sleep(1)
			print("Congratulations! You won the match in {} rounds! \n".format(game_round))

		if comp_wins >= 2:
			time.sleep(1)
			print("The computer won the match in {} rounds. \n".format(game_round))
			break


def compare(playerChoice, compChoice):
	if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
		print("That is not a valid choice.")
		playerChoice = input("Please select 'rock', 'paper', or 'scissors' ")
		
		if playerChoice == compChoice:
			# PICK UP HERE. The else statement below throws an error on a tie.

		else:
			compare(playerChoice, compChoice) #recursion

	


	else:
		results = {("rock", "paper") : False,
				   ("rock", "scissors") : True,
				   ("paper", "scissors") : False,
				   ("paper", "rock") : True,
				   ("scissors", "rock") : False,
				   ("scissors", "paper") : True}
		return results[(playerChoice,compChoice)]


while play_condition != "exit":
	play_match()
	play_condition = input("Do you want to play again? Type 'exit' to exit the game or hit enter to play a round. ".format(player_name))

print("Until next time! \n")