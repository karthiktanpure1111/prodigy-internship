import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🎮 Guess the Number!")
        self.master.geometry("450x350")
        self.master.configure(bg="#f0f8ff")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(master, text="🔢 I'm thinking of a number between 1 and 100", 
                                    font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#333")
        self.title_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 14), justify='center', width=10)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Check Guess", font=("Helvetica", 12), bg="#90ee90", 
                                      command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f8ff", fg="#444")
        self.feedback_label.pack(pady=10)

        self.attempt_label = tk.Label(master, text="Attempts: 0", font=("Helvetica", 12), bg="#f0f8ff", fg="#444")
        self.attempt_label.pack(pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", font=("Helvetica", 12), bg="#87cefa", 
                                           command=self.restart_game)
        self.play_again_button.pack(pady=10)

    def check_guess(self):
        guess_text = self.entry.get()
        if not guess_text.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 100.")
            return

        guess = int(guess_text)
        self.attempts += 1
        self.attempt_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.feedback_label.config(text="📉 Too low! Try a higher number.")
        elif guess > self.secret_number:
            self.feedback_label.config(text="📈 Too high! Try a lower number.")
        else:
            self.feedback_label.config(text=f"🎉 Correct! The number was {self.secret_number}.")
            messagebox.showinfo("You Win!", f"🥳 You guessed the number in {self.attempts} attempts!")
            self.guess_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.attempt_label.config(text="Attempts: 0")
        self.guess_button.config(state=tk.NORMAL)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
