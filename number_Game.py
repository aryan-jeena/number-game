import tkinter as tk
from tkinter import messagebox
import random

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Game")
        
        # Set the window size to 900x700 for a larger display
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        self.player1_points = 20
        self.player2_points = 20
        self.player1_wins = 0
        self.player2_wins = 0
        self.round = 1
        self.current_player = None
        self.tiebreaker_winner = random.choice(["Player 1", "Player 2"])
        self.player1_input = None
        self.player2_input = None
        
        # Configure fonts for labels and buttons
        self.label_font = ("Arial", 16)
        self.entry_font = ("Arial", 14)
        self.button_font = ("Arial", 14, "bold")
        
        # Round history to track and display winners
        self.round_history = []
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame to center all content
        frame = tk.Frame(self.root)
        frame.pack(expand=True)
        
        # Display initial tiebreaker winner
        self.tiebreaker_label = tk.Label(frame, text=f"{self.tiebreaker_winner} wins the coin flip and will go first.", font=self.label_font)
        self.tiebreaker_label.pack(pady=(0, 10))

        # Round info
        self.round_label = tk.Label(frame, text=f"Round {self.round}", font=self.label_font)
        self.round_label.pack(pady=(0, 10))

        # Player info labels
        self.player1_label = tk.Label(frame, text=f"Player 1: {self.player1_points} points remaining", font=self.label_font)
        self.player1_label.pack()
        self.player2_label = tk.Label(frame, text=f"Player 2: {self.player2_points} points remaining", font=self.label_font)
        self.player2_label.pack()

        # Entry field for player input
        self.player_entry_label = tk.Label(frame, text="", font=self.label_font)
        self.player_entry_label.pack(pady=(20, 5))
        self.player_entry = tk.Entry(frame, font=self.entry_font, justify="center", width=10)
        self.player_entry.pack()
        self.player_entry.bind("<Return>", lambda event: self.submit_points())

        # Submit button
        self.submit_button = tk.Button(frame, text="Submit Points", font=self.button_font, command=self.submit_points)
        self.submit_button.pack(pady=20)

        # Result display
        self.result_label = tk.Label(frame, text="", font=self.label_font)
        self.result_label.pack(pady=(10, 0))

        # Round history label
        self.round_history_label = tk.Label(frame, text="Round History:", font=self.label_font)
        self.round_history_label.pack(pady=(20, 5))
        self.round_history_display = tk.Label(frame, text="", font=self.entry_font, justify="left")
        self.round_history_display.pack()

        # Initialize the current player based on tiebreaker
        self.current_player = self.tiebreaker_winner
        self.update_player_prompt()

    def update_player_prompt(self):
        # Update prompt based on the current player
        self.player_entry_label.config(text=f"{self.current_player}, enter your points:")
    
    def switch_player(self):
        # Switch to the other player
        self.current_player = "Player 1" if self.current_player == "Player 2" else "Player 2"
        self.update_player_prompt()

    def submit_points(self):
        try:
            points = int(self.player_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        # Validate points based on the current player
        if self.current_player == "Player 1":
            if points > self.player1_points:
                messagebox.showerror("Invalid Points", "Player 1 cannot bet more points than they have remaining.")
                return
            self.player1_input = points
        elif self.current_player == "Player 2":
            if points > self.player2_points:
                messagebox.showerror("Invalid Points", "Player 2 cannot bet more points than they have remaining.")
                return
            self.player2_input = points

        # Clear entry and switch player or determine round winner
        self.player_entry.delete(0, tk.END)

        if self.player1_input is not None and self.player2_input is not None:
            # Both players have entered points, determine winner
            self.determine_round_winner()
        else:
            # Switch to the next player
            self.switch_player()

    def determine_round_winner(self):
        if self.player1_input > self.player2_input:
            round_result = "Player 1 wins the round!"
            self.player1_wins += 1
        elif self.player2_input > self.player1_input:
            round_result = "Player 2 wins the round!"
            self.player2_wins += 1
        else:
            if self.tiebreaker_winner == "Player 1":
                round_result = "Player 1 wins the tie!"
                self.player1_wins += 1
                self.tiebreaker_winner = "Player 2"  # Switch tiebreaker for next tie
            else:
                round_result = "Player 2 wins the tie!"
                self.player2_wins += 1
                self.tiebreaker_winner = "Player 1"

        # Update points remaining
        self.player1_points -= self.player1_input
        self.player2_points -= self.player2_input

        # Update labels
        self.player1_label.config(text=f"Player 1: {self.player1_points} points remaining")
        self.player2_label.config(text=f"Player 2: {self.player2_points} points remaining")
        self.result_label.config(text=round_result)
        
        # Update round history
        self.round_history.append(f"Round {self.round}: {round_result}")
        self.round_history_display.config(text="\n".join(self.round_history))

        # Reset inputs for the next round
        self.player1_input = None
        self.player2_input = None

        # Check if a player has won 4 rounds and end the game early if so
        if self.player1_wins == 4 or self.player2_wins == 4:
            self.end_game()
        else:
            # Move to the next round if the game isn't over
            if self.round < 7:
                self.round += 1
                self.round_label.config(text=f"Round {self.round}")
                self.current_player = self.tiebreaker_winner  # Reset to tiebreaker winner for each round
                self.update_player_prompt()

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
