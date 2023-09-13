#Exercise from https://www.practicepython.org/
#Efficient example using dictionaries and functions: https://codereview.stackexchange.com/questions/172337/rock-paper-scissors-game-in-python
#Styleguide reference: https://peps.python.org/pep-0008/

import random 

print("Welcome to Rock, Paper, Scissors Classic! Compete against the computer in a best of 3 and win fabulous prizes!")
player_name = input("What is your name? ")
play_condition = input("Welcome {}. Type 'exit' to exit the game or hit enter to play a round. ".format(player_name))

def play_round()
	game_round = 1
	while game_round <= 3:
		player_wins = 0
		playerChoice = input("{}: Select 'rock', 'paper', or 'scissors' ".format(player_name))
		compChoice = random.randint(0,2)
		compare(playerChoice, compChoice)


		print("The computer threw {}. You win round {}".format(compChoice, game_round))
		game_round += 1

		if game_round == 2 and player_wins == 2:
			print("Congratulations! You've won this round!")
			game_round = 10


def compare(playerChoice, compChoice)
	rps_conditions = {(rock, paper) : False,
				      (rock, scissors) : True,
				      (paper, scissors) : False,
				      (paper, rock) : True,
				      (scissors, rock) : False,
				      (scissors, paper) : True}
	return results[(playerChoice,compChoice)]


while play_condition != "exit":
	play_round()
	play_condition = input("Do you want to play again? Type 'exit' to exit the game or hit enter to play a round. ".format(player_name))

print("Until next time!")
