import tkinter as tk
from tkinter import messagebox


def on_button_click(i, j):
    global current_player
    button = buttons[i][j]
    if button["text"] == "" and not game_over:
        button.config(text=current_player)
        check_for_winner()
        current_player = "O" if current_player == "X" else "X"


def check_for_winner():
    # Add logic here to check if a player has won and update game_over
    global game_over
    # Check rows
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            != ""
        ):
            messagebox.showinfo(
                "Tic Tac Toe", f"Player {buttons[row][0]['text']} wins!"
            )
            game_over = True
            return

    # Check columns
    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            != ""
        ):
            messagebox.showinfo(
                "Tic Tac Toe", f"Player {buttons[0][col]['text']} wins!"
            )
            game_over = True
            return

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        messagebox.showinfo("Tic Tac Toe", f"Player {buttons[0][0]['text']} wins!")
        game_over = True
        return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        messagebox.showinfo("Tic Tac Toe", f"Player {buttons[0][2]['text']} wins!")
        game_over = True
        return

    # Check for a draw
    if all(button["text"] != "" for row in buttons for button in row):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        game_over = True


# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables
current_player = "X"
game_over = False

# Initialize a 3x3 list to store buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create the buttons and add them to the window
for i in range(3):
    for j in range(3):
        button = tk.Button(
            root,
            text="",
            font=("normal", 40),
            width=5,
            height=2,
            command=lambda i=i, j=j: on_button_click(i, j),
        )
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = button  # Store the button in the list

# Start the Tkinter event loop
root.mainloop()
