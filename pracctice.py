import tkinter as tk
from tkinter import messagebox
import random

# ----- GAME LOGIC -----
class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("350x400")

        self.wins = 0
        self.losses = 0

        self.setup_widgets()
        self.reset_game()

    def setup_widgets(self):
        self.title_label = tk.Label(self.master, text="Guess the number (1–100)", font=("Arial", 14))
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.hint_button = tk.Button(self.master, text="Hint", font=("Arial", 10), command=self.give_hint)
        self.hint_button.pack(pady=5)

        self.restart_button = tk.Button(self.master, text="Restart", font=("Arial", 10), command=self.reset_game)
        self.restart_button.pack(pady=5)

        self.score_label = tk.Label(self.master, text="Wins: 0 | Losses: 0", font=("Arial", 11))
        self.score_label.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showwarning("⚠️ Invalid Input", "Please enter a valid number!")
            return

        guess = int(guess)
        self.attempts += 1

        if guess > self.number:
            self.result_label.config(text="Too high 📈")
        elif guess < self.number:
            self.result_label.config(text="Too low 📉")
        else:
            self.result_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} tries.")
            self.wins += 1
            self.end_game()
            return

        if self.attempts == 3:
            self.give_hint()

        if self.attempts >= self.max_attempts and guess != self.number:
            self.result_label.config(text=f"😢 Out of attempts! Number was {self.number}")
            self.losses += 1
            self.end_game()

    def give_hint(self):
        hint = "Hint:\n"
        hint += "Even\n" if self.number % 2 == 0 else "Odd\n"
        hint += "Greater than 50" if self.number > 50 else "50 or less"
        messagebox.showinfo("Hint", hint)

    def end_game(self):
        self.guess_button.config(state="disabled")
        self.update_score()

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.guess_button.config(state="normal")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Wins: {self.wins} | Losses: {self.losses}")

# ----- RUNNING THE APP -----
root = tk.Tk()
app = NumberGuessingGame(root)
root.mainloop()
