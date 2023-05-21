#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:37:29 2023

@author: aryanjeena
"""

import random

player1_points = 20
player2_points = 20
player1_wins = 0
player2_wins = 0

# Perform a coin flip to determine the tiebreaker winner
tiebreaker_winner = random.choice(["Player 1", "Player 2"])
print(f"{tiebreaker_winner} wins the coin flip and will win the first tie.")

for round in range(1, 8):
    print(f"Round {round}")
    print(f"Player 1: {player1_points} points remaining")
    print(f"Player 2: {player2_points} points remaining")

    # Get player 1's input
    player1_input = int(input("Player 1, how many points will you put in? "))
    while player1_input > player1_points:
        player1_input = int(input("You don't have enough points, try again: "))

    # Add 20 spaces using a loop
    for line in range(20):
        print("\n")

    # Get player 2's input
    player2_input = int(input("Player 2, how many points will you put in? "))
    while player2_input > player2_points:
        player2_input = int(input("You don't have enough points, try again: "))

    # Add 20 spaces using a loop
    for line in range(20):
        print("\n")

    # Determine the winner of the round
    if player1_input > player2_input:
        print("Player 1 wins the round!")
        player1_wins += 1
    elif player2_input > player1_input:
        print("Player 2 wins the round!")
        player2_wins += 1

    else:
        # There's a tie, so determine the winner based on the tiebreaker winner
        if tiebreaker_winner == "Player 1":
            print("Player 1 wins the tie!")
            player1_wins += 1
            tiebreaker_winner = "Player 2"
        else:
            print("Player 2 wins the tie!")
            player2_wins += 1
            tiebreaker_winner = "Player 1"

    print()  # Print a blank line
    player2_points -= player2_input
    player1_points -= player1_input

# Determine the winner of the game
if player1_wins > player2_wins:
    print("Player 1 wins the game!")
elif player2_wins > player1_wins:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")

print(f"Final score: Player 1: {player1_wins}, Player 2: {player2_wins}")
