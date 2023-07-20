import random
import tkinter as tk
from tkinter import messagebox

attempts_list = []


def show_score():
    if not attempts_list:
        messagebox.showinfo('High Score', 'There is currently no high score. It\'s yours for the taking!')
    else:
        messagebox.showinfo('High Score', f'The current high score is {min(attempts_list)} attempts')


def check_guess(guess, rand_num, attempts):
    if guess == rand_num:
        messagebox.showinfo('Guess Result', f'Nice! You got it!\nIt took you {attempts} attempts')
        return True
    elif guess > rand_num:
        messagebox.showinfo('Guess Result', 'It\'s lower')
    else:
        messagebox.showinfo('Guess Result', 'It\'s higher')
    return False


def play_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    player_name = entry_name.get().strip()

    if not player_name:
        messagebox.showwarning('Player Name', 'Please enter your name!')
        return

    wanna_play = messagebox.askquestion('Start Game', f'Hi, {player_name}, would you like to play the guessing game?')

    if wanna_play == 'no':
        messagebox.showinfo('Game Over', 'That\'s cool, Thanks!')
        root.destroy()
        return

    show_score()

    def submit_guess(event=None):
        nonlocal attempts, rand_num, player_name
        try:
            guess = int(entry_guess.get())
            if guess < 1 or guess > 10:
                raise ValueError('Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if check_guess(guess, rand_num, attempts):
                wanna_play = messagebox.askquestion('Play Again', 'Would you like to play again?')
                if wanna_play == 'no':
                    messagebox.showinfo('Game Over', 'That\'s cool, have a good one!')
                    root.destroy()
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    entry_guess.delete(0, tk.END)
        except ValueError:
            messagebox.showerror('Invalid Input', 'Oh no! That is not a valid value. Try again...')
            entry_guess.delete(0, tk.END)

    label_guess = tk.Label(root, text='Enter your guess (1-10):')
    label_guess.pack(pady=10)

    entry_guess = tk.Entry(root)
    entry_guess.pack()

    entry_guess.focus()

    root.bind('<Return>', submit_guess)


root = tk.Tk()
root.title('Number Guessing Game')

label_name = tk.Label(root, text='What is your name?')
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

button_start = tk.Button(root, text='Start Game', command=play_game)
button_start.pack(pady=10)

root.mainloop()
