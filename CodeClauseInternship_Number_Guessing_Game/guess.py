import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.label = tk.Label(self.root, text="Guess the number between 1 and 100:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        self.attempts += 1
        guess = int(self.entry.get())
        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", f"You've guessed the number {self.secret_number} in {self.attempts} attempts!")
            self.root.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Incorrect", "o no it is low! Try again.")
        else:
            messagebox.showinfo("Incorrect", "o no it is high! Try again.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.root.mainloop()
