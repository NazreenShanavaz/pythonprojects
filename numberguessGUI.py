import tkinter as tk
import random
from tkinter import messagebox


root = tk.Tk()
root.title('Number Guessing Game')
root.geometry("300x400")

number=random.randint(1,100)
attempt=0
max_attempt=5

def give_hint():
    hint = ""
    if number % 2 == 0:
        hint += "Hint: Number is even\n"
    else:
        hint += "Hint: Number is odd\n"

    if number > 50:
        hint += "Hint: Number is greater than 50"
    else:
        hint += "Hint: Number is 50 or less"

    messagebox.showinfo("Hint", hint)

def guess_check():
    guess=entry.get()
    global attempt

    if not guess.isdigit():
        result_label.config(text="enter a valid number")
        return

    guess=int(guess)
    attempt+=1


    if guess>number:
        result_label.config(text="too high")
    elif guess<number:
        result_label.config(text="too low")
    else:
        result_label.config(text="CORRECT!!")

    if attempt == 3:
        give_hint()

    if attempt >= max_attempt:
        result_label.config(text=f"Game Over! Number was {number}")
        guess_button.config(state="disabled")

def restart_game():
    global number, attempt
    number = random.randint(1, 100)
    attempt = 0
    entry.delete(0, tk.END)
    result_label.config(text="")
    guess_button.config(state="normal")

title_label = tk.Label(root, text="Enter a number (1-100)", font=("Arial", 14))
title_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=("Arial", 14),command=guess_check)
guess_button.pack(pady=10)

result_label=tk.Label(root,font=("Arial", 14))
result_label.pack(pady=20)

restart_button = tk.Button(root, text="Restart", font=("Arial", 10), command=restart_game)
restart_button.pack(pady=5)

root.mainloop()
