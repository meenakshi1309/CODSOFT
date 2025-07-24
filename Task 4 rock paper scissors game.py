import tkinter as tk
import random

# Setup main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x640")
root.config(bg="#1e1e1e")

# Game variables
user_score = 0
comp_score = 0
rounds_played = 0
max_rounds = 5
choices = ["Rock", "Paper", "Scissors"]

# UI Colors
primary_color = "#8e44ad"
text_color = "white"
button_bg = "#2e2e2e"
player_color = "#00ff99"
computer_color = "#ff6b6b"
tie_color = "#ffd700"
win_color = "#00d9ff"
lose_color = "#ff3333"

# Reset function
def reset_game():
    global user_score, comp_score, rounds_played
    user_score = 0
    comp_score = 0
    rounds_played = 0
    result_you.config(text="")
    result_comp.config(text="")
    result_final.config(text="Make your move!", fg=text_color)
    user_score_label.config(text="Your Score: 0")
    comp_score_label.config(text="Computer Score: 0")
    scoreboard.delete(0, tk.END)
    listbox.delete(0, tk.END)
    view_frame.pack_forget()
    main_frame.pack()

# Done button function
def mark_done():
    reset_game()

# Main play function
def play(user_choice):
    global user_score, comp_score, rounds_played

    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie!"
        result_final.config(fg=tie_color)
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        user_score += 1
        result = "You Win!"
        result_final.config(fg=win_color)
    else:
        comp_score += 1
        result = "Computer Wins!"
        result_final.config(fg=lose_color)

    rounds_played += 1

    result_you.config(text=f"You:       {user_choice}", fg=player_color)
    result_comp.config(text=f"Computer:  {comp_choice}", fg=computer_color)
    result_final.config(text=result)

    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer Score: {comp_score}")
    scoreboard.insert(tk.END, f"{user_choice} vs {comp_choice} ➤ {result}")
    listbox.insert(tk.END, f"{user_choice} vs {comp_choice} ➤ {result}")

    if rounds_played == max_rounds:
        main_frame.pack_forget()
        if user_score > comp_score:
            congrats_label.config(text="Congratulations! You won the match!", bg="#1abc9c")
        elif comp_score > user_score:
            congrats_label.config(text="Computer won the match. Try again!", bg="#e74c3c")
        else:
            congrats_label.config(text="It's a draw!", bg="#f39c12")
        view_frame.pack()

# ========== Main Frame ==========
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack()

tk.Label(main_frame, text="Rock Paper Scissors",
         font=("Helvetica", 16, "bold"),
         fg=primary_color, bg="#1e1e1e").pack(pady=10)

tk.Label(main_frame, text="Play 5 rounds to finish the match!",
         font=("Helvetica", 11),
         fg=text_color, bg="#1e1e1e").pack(pady=(0, 12))

# Vertical label
tk.Label(main_frame,
         text="Rock\nPaper\nScissors",
         font=("Helvetica", 14, "bold"),
         fg="#9b59b6",
         bg="#1e1e1e",
         justify="center").pack(pady=8)

# Result Labels
result_you = tk.Label(main_frame, text="", font=("Helvetica", 10, "bold"), bg="#1e1e1e")
result_you.pack()
tk.Label(main_frame, text="", font=("Helvetica", 1), bg="#1e1e1e").pack(pady=6)
result_comp = tk.Label(main_frame, text="", font=("Helvetica", 10, "bold"), bg="#1e1e1e")
result_comp.pack()
result_final = tk.Label(main_frame, text="Make your move!", font=("Helvetica", 11, "bold"),
                        fg=text_color, bg="#1e1e1e")
result_final.pack(pady=10)

# Score Display inside a frame with border and shadow
score_shadow = tk.Frame(main_frame, bg="#000000")
score_shadow.pack(pady=10)
score_box = tk.Frame(score_shadow, bg="#2c3e50", padx=10, pady=6, bd=2, relief="ridge")
score_box.pack()

user_score_label = tk.Label(score_box, text="Your Score: 0",
                            font=("Helvetica", 10), fg=text_color, bg="#2c3e50")
user_score_label.pack(side="left", padx=25)
comp_score_label = tk.Label(score_box, text="Computer Score: 0",
                            font=("Helvetica", 10), fg=text_color, bg="#2c3e50")
comp_score_label.pack(side="right", padx=25)

# Vertical Buttons
button_frame = tk.Frame(main_frame, bg="#1e1e1e")
button_frame.pack(pady=15)
for choice in choices:
    tk.Button(button_frame, text=choice, width=20, height=1,
              font=("Helvetica", 10), fg=text_color, bg=button_bg,
              activebackground=primary_color,
              command=lambda c=choice: play(c)).pack(pady=5)

# Scoreboard
tk.Label(main_frame, text="Scoreboard",
         font=("Helvetica", 10, "bold"), fg=primary_color, bg="#1e1e1e").pack(pady=(15, 5))
scoreboard = tk.Listbox(main_frame, height=6, width=42,
                        font=("Helvetica", 9), bg="#2a2a2a", fg="white")
scoreboard.pack(pady=5)

# ========== Congrats View ==========
view_frame = tk.Frame(root, bg="#1e1e1e")
tk.Label(view_frame, text="Round Summary",
         font=("Helvetica", 11, "bold"), fg="yellow", bg="#1e1e1e").pack(pady=10)
listbox = tk.Listbox(view_frame, width=40, height=10,
                     bg="yellow", fg="black", font=("Helvetica", 10))
listbox.pack(pady=5)
congrats_label = tk.Label(view_frame, text="",
                          fg="white", bg="#1abc9c",
                          font=("Helvetica", 9, "bold"), padx=10, pady=8)
congrats_label.pack(pady=12)
tk.Button(view_frame, text="Mark Done", command=mark_done).pack(pady=5)

# Start GUI
root.mainloop()
