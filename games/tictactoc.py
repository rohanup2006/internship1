import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9
buttons = []
win_combos = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

def check_winner():
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if all(cell != "" for cell in board):
        return "Draw"
    return None

def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", state=tk.NORMAL)

def on_button_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        result = check_winner()
        if result:
            if result == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"{result} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

root = tk.Tk()
root.title("Tic Tac Toe")
for i in range(9):
    button = tk.Button(root, text="", width=10, height=5, command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()

