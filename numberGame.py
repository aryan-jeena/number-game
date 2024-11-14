#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:37:29 2023

@author: aryanjeena
"""

import tkinter as tk
from tkinter import messagebox
import random

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Game")
        
        self.player1_points = 20
        self.player2_points = 20
        self.player1_wins = 0
        self.player2_wins = 0
        self.round = 1
        self.tiebreaker_winner = random.choice(["Player 1", "Player 2"])
        
        self.setup_ui()
    
    def setup_ui(self):
        # Display initial tiebreaker winner
        self.tiebreaker_label = tk.Label(self.root, text=f"{self.tiebreaker_winner} wins the coin flip and will win the first tie.")
        self.tiebreaker_label.grid(row=0, column=0, columnspan=2)

        # Round info
        self.round_label = tk.Label(self.root, text=f"Round {self.round}")
        self.round_label.grid(row=1, column=0, columnspan=2)

        # Player 1 info
        self.player1_label = tk.Label(self.root, text=f"Player 1: {self.player1_points} points remaining")
        self.player1_label.grid(row=2, column=0)
        self.player1_entry = tk.Entry(self.root)
        self.player1_entry.grid(row=3, column=0)

        # Player 2 info
        self.player2_label = tk.Label(self.root, text=f"Player 2: {self.player2_points} points remaining")
        self.player2_label.grid(row=2, column=1)
        self.player2_entry = tk.Entry(self.root)
        self.player2_entry.grid(row=3, column=1)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit Points", command=self.submit_points)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        # Result display
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def submit_points(self):
        try:
            player1_input = int(self.player1_entry.get())
            player2_input = int(self.player2_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for both players.")
            return
        
        # Validate points
        if player1_input > self.player1_points or player2_input > self.player2_points:
            messagebox.showerror("Invalid Points", "Players cannot bet more points than they have remaining.")
            return

        # Clear entries for next round
        self.player1_entry.delete(0, tk.END)
        self.player2_entry.delete(0, tk.END)

        # Determine the round winner
        if player1_input > player2_input:
            round_result = "Player 1 wins the round!"
            self.player1_wins += 1
        elif player2_input > player1_input:
            round_result = "Player 2 wins the round!"
            self.player2_wins += 1
        else:
            # Tie - use tiebreaker
            if self.tiebreaker_winner == "Player 1":
                round_result = "Player 1 wins the tie!"
                self.player1_wins += 1
                self.tiebreaker_winner = "Player 2"
            else:
                round_result = "Player 2 wins the tie!"
                self.player2_wins += 1
                self.tiebreaker_winner = "Player 1"
        
        # Update points
        self.player1_points -= player1_input
        self.player2_points -= player2_input

        # Update labels
        self.player1_label.config(text=f"Player 1: {self.player1_points} points remaining")
        self.player2_label.config(text=f"Player 2: {self.player2_points} points remaining")
        self.result_label.config(text=round_result)

        # Check if game is over
        if self.round == 7:
            self.end_game()
        else:
            self.round += 1
            self.round_label.config(text=f"Round {self.round}")

    def end_game(self):
        if self.player1_wins > self.player2_wins:
            final_result = "Player 1 wins the game!"
        elif self.player2_wins > self.player1_wins:
            final_result = "Player 2 wins the game!"
        else:
            final_result = "It's a tie!"
        
        final_score = f"Final score: Player 1: {self.player1_wins}, Player 2: {self.player2_wins}"
        messagebox.showinfo("Game Over", f"{final_result}\n{final_score}")
        self.root.destroy()

# Run the GUI
root = tk.Tk()
game_gui = GameGUI(root)
root.mainloop()
