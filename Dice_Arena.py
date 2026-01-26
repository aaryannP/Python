import tkinter as tk
import random
from tkinter import messagebox

BLOCKS = 50
SAFE_BLOCKS = [6, 19, 27, 40, 48]

reward_blocks = []
while len(reward_blocks) < 3:
    r = random.randint(1, 50)
    if r not in reward_blocks and r not in SAFE_BLOCKS:
        reward_blocks.append(r)

players = [
    {"pos": 0, "points": 0},
    {"pos": 0, "points": 0}
]

current_player = 0
game_over = False

root = tk.Tk()
root.title("50 Block Ludo Game")
root.resizable(False, False)

board_frame = tk.Frame(root)
board_frame.grid(row=0, column=1, padx=10)

left_panel = tk.Frame(root)
left_panel.grid(row=0, column=0, padx=10)

right_panel = tk.Frame(root)
right_panel.grid(row=0, column=2, padx=10)

p1_pos_label = tk.Label(left_panel, text="Position: 0")
p1_points_label = tk.Label(left_panel, text="Points: 0")
p1_pos_label.pack()
p1_points_label.pack()

p2_pos_label = tk.Label(right_panel, text="Position: 0")
p2_points_label = tk.Label(right_panel, text="Points: 0")
p2_pos_label.pack()
p2_points_label.pack()

blocks = {}

for i in range(1, BLOCKS + 1):
    bg = "white"
    if i in SAFE_BLOCKS:
        bg = "green"
    if i in reward_blocks:
        bg = "yellow"

    lbl = tk.Label(
        board_frame,
        text=str(i),
        width=6,
        height=3,
        relief="solid",
        bg=bg
    )
    lbl.grid(row=(i - 1) // 5, column=(i - 1) % 5, padx=2, pady=2)
    blocks[i] = lbl

control_frame = tk.Frame(root)
control_frame.grid(row=1, column=0, columnspan=3, pady=10)

dice_label = tk.Label(control_frame, text="Dice: -")
dice_label.pack()

turn_label = tk.Label(control_frame, text="Turn: User 1")
turn_label.pack()

def update_board():
    for i in range(1, BLOCKS + 1):
        if i in SAFE_BLOCKS:
            blocks[i].config(bg="#d4f5d4")
        elif i in reward_blocks:
            blocks[i].config(bg="#ffeeba")
        else:
            blocks[i].config(bg="white")

    if players[0]["pos"] > 0:
        blocks[players[0]["pos"]].config(bg="#ff5252")

    if players[1]["pos"] > 0:
        blocks[players[1]["pos"]].config(bg="#4285f4")

    p1_pos_label.config(text=f"Position: {players[0]['pos']}")
    p1_points_label.config(text=f"Points: {players[0]['points']}")
    p2_pos_label.config(text=f"Position: {players[1]['pos']}")
    p2_points_label.config(text=f"Points: {players[1]['points']}")

def roll_dice():
    global current_player, game_over

    if game_over:
        return

    dice = random.randint(1, 6)
    dice_label.config(text=f"Dice: {dice}")

    player = players[current_player]
    new_pos = player["pos"] + dice

    if new_pos > 50:
        current_player = 1 - current_player
        turn_label.config(text=f"Turn: User {current_player + 1}")
        return

    player["pos"] = new_pos

    if new_pos in reward_blocks:
        player["points"] += 1
        reward_blocks.remove(new_pos)

    other = 1 - current_player
    if (
        players[other]["pos"] == player["pos"]
        and player["pos"] not in SAFE_BLOCKS
    ):
        back_pos = players[other]["points"] * 5
        if back_pos < 1:
            back_pos = 1
        if back_pos >= players[other]["pos"]:
            back_pos = 1
        players[other]["pos"] = back_pos

    update_board()

    if player["pos"] == 50:
        messagebox.showinfo("Game Over", f"User {current_player + 1} Wins!")
        game_over = True
        return

    current_player = other
    turn_label.config(text=f"Turn: User {current_player + 1}")

dice_button = tk.Button(control_frame, text="🎲 Roll Dice", command=roll_dice)
dice_button.pack(pady=5)

update_board()
root.mainloop()