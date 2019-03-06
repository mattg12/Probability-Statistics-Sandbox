# St Petersburg Paradox
# Generate an arbitrary number of trials of the St Petersburg Paradox Game
# For each trial, return - given an initial price - the profit or loss from the entire game

import random
import matplotlib.pyplot as plt
import scipy.stats as stats

# define a single instance of the game
def st_petersburg(price):
	pot = 2
	price = price
	coin = 'heads'
	heads = 0
	while coin == 'heads':
		flip = random.randint(0,1)
		if flip == 1:
			pot *= 2
			heads +=1
		else:
			coin = 'tails'
    profits = pot - price
	return heads, profit

# Simulation - demonstrate a number of possible outcomes
def st_petersburg_simulation():
	price = int(input("What price? "))
	_,bets = [st_petersburg(price) for i in range(10000)]
	max_win = max(bets)
	min_win= min(bets)
	print("Max Profit: {} \nMin Profit: {} \n".format(max_win,min_win))
	print(stats.describe(bets))
	plt.hist(bets)
    plt.title("Simulation of 10000 trials of St. Petersburg Game")
    plt.ylabel("Profits")
    plt.xlabel("Number of Observations")
	plt.show()

# Demonstration - play the game repeatedly
def st_petersburg_game(player_bank = 100, casino_bank = 100000000):
    price = int(input("How much will you pay to play? "))
    strategy = input("play one game [p] or let it ride [r]? ")
    num_games = 0

    if strategy == 'p':
    	while player_bank >  0 and casino_bank > 0:
    		game = input("Play? [y]/[n]")
    		if game == 'y':
        		player_bank += st_petersburg(price)
        		casino_bank -= st_petersburg(price)
        		num_games +=1
        		print("Player bank: {} \nCasinoBank: {} \nGames: {}".format(player_bank,casino_bank,num_games))
    elif strategy == 'r':
        while player_bank > 0 and casino_bank > 0:
        	player_bank += st_petersburg(price)
        	casino_bank -= st_petersburg(price)
        	num_games += 1

    if player_bank <= 0:
        print("You are bankrupt after {} games!".format(num_games))
    if casino_bank <= 0:
    	print("You broke the casino after {} games!\nYou won {}!".format(num_games, (player_bank - price)))

# Prompt user to see a demo or play a game
def choose_adventure():
    choice = input("Choose: Game [g] or Simulation [s]? ")
    if choice == 'g':
    	st_petersburg_game()
    elif choice == 's':
    	st_petersburg_simulation()

choose_adventure()
