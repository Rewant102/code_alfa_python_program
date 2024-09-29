import tkinter as tk
from tkinter import messagebox
import random

# Hangman Game class
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x400")

        # Word list for the game
        self.word_list = ['python', 'hangman', 'development', 'programming', 'algorithm']
        self.word = random.choice(self.word_list).upper()  # Randomly chosen word
        self.word_display = ['_' for _ in self.word]  # Display as underscores

        # Variables to track game state
        self.guessed_letters = []
        self.lives = 6

        # GUI elements
        self.label_word = tk.Label(self.root, text=" ".join(self.word_display), font=("Arial", 20))
        self.label_word.pack(pady=20)

        self.label_lives = tk.Label(self.root, text=f"Lives Remaining: {self.lives}", font=("Arial", 14))
        self.label_lives.pack()

        self.label_input = tk.Label(self.root, text="Enter a letter:", font=("Arial", 12))
        self.label_input.pack(pady=10)

        self.entry_guess = tk.Entry(self.root, font=("Arial", 12), justify='center', width=5)
        self.entry_guess.pack()

        self.button_guess = tk.Button(self.root, text="Guess", command=self.guess_letter)
        self.button_guess.pack(pady=10)

        self.button_restart = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.button_restart.pack(pady=10)

    def guess_letter(self):
        guess = self.entry_guess.get().upper()
        self.entry_guess.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed the letter '{guess}'")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[i] = guess
            self.label_word.config(text=" ".join(self.word_display))
        else:
            self.lives -= 1
            self.label_lives.config(text=f"Lives Remaining: {self.lives}")

        if "_" not in self.word_display:
            messagebox.showinfo("Congratulations!", "You guessed the word!")
            self.disable_input()
        elif self.lives == 0:
            messagebox.showerror("Game Over", f"You've run out of lives! The word was '{self.word}'")
            self.disable_input()

    def disable_input(self):
        self.entry_guess.config(state=tk.DISABLED)
        self.button_guess.config(state=tk.DISABLED)

    def restart_game(self):
        self.word = random.choice(self.word_list).upper()
        self.word_display = ['_' for _ in self.word]
        self.guessed_letters = []
        self.lives = 6
        self.label_word.config(text=" ".join(self.word_display))
        self.label_lives.config(text=f"Lives Remaining: {self.lives}")
        self.entry_guess.config(state=tk.NORMAL)
        self.button_guess.config(state=tk.NORMAL)


# Run the tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
