import tkinter as tk

history = []

def click(char):
    if char == "C":
        update_display("")
    elif char == "⌫":
        current = display_text.get("1.0", tk.END).strip()
        update_display(current[:-1])
    elif char == "()":
        current = display_text.get("1.0", tk.END).strip()
        if current.count("(") == current.count(")"):
            update_display(current + "(")
        else:
            update_display(current + ")")
    elif char == "=":
        try:
            expression = display_text.get("1.0", tk.END).strip().replace("×", "*").replace("÷", "/")
            result = str(eval(expression))
            history.append(f"{expression} = {result}")
            if len(history) > 10:
                history.pop(0)
            refresh_history()
            show_expression_with_result(expression, result)
        except:
            update_display("Error")
    elif char == "±":
        try:
            value = float(eval(display_text.get("1.0", tk.END)))
            update_display(str(-value))
        except:
            update_display("Error")
    else:
        update_display(display_text.get("1.0", tk.END).strip() + char)

def update_display(content):
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, content)
    display_text.tag_config("white", foreground="white")
    display_text.tag_add("white", "1.0", tk.END)
    display_text.mark_set(tk.INSERT, "end-1c")

def show_expression_with_result(expression, result):
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, expression + "\n", "white")
    display_text.insert(tk.END, result, "purple")
    display_text.tag_config("white", foreground="white")
    display_text.tag_config("purple", foreground="#A066D3")
    display_text.mark_set(tk.INSERT, "end-1c")

def refresh_history():
    history_box.delete(0, tk.END)
    for item in reversed(history):
        history_box.insert(tk.END, item)

def select_history(event):
    selected = history_box.curselection()
    if selected:
        selected_text = history_box.get(selected[0])
        expression = selected_text.split('=')[0].strip()
        update_display(expression)

def disable_input(event):
    return "break"

# Main Window Setup
root = tk.Tk()
root.title("Meenu's Pro Calculator")
root.geometry("360x640")
root.config(bg="black")
root.resizable(False, False)

# Display Text Field (Cursor enabled)
display_text = tk.Text(
    root,
    height=2,
    font=("Helvetica", 24),
    bg="black",
    fg="white",
    bd=0,
    relief="flat",
    wrap="word",
    insertbackground="white",  # Show white blinking cursor
    cursor="xterm"             # Enable standard text cursor
)
display_text.pack(fill="x", padx=10, pady=(15, 5))
display_text.insert(tk.END, "")
display_text.bind("<Key>", disable_input)
display_text.bind("<Button-1>", disable_input)
display_text.bind("<ButtonRelease-1>", disable_input)
display_text.bind("<B1-Motion>", disable_input)

# Prevent Zooming
root.bind_all("<Control-MouseWheel>", disable_input)
root.bind_all("<Control-plus>", disable_input)
root.bind_all("<Control-minus>", disable_input)

# History Label
tk.Label(root, text="History", font=("Helvetica", 10), fg="white", bg="black").pack(anchor="w", padx=12)

# History Box
history_box = tk.Listbox(root, height=6, font=("Courier", 10),
                         bg="#1A1A1A", fg="white", bd=0, selectbackground="#A066D3")
history_box.pack(fill="x", padx=10, pady=(0, 12))
history_box.bind("<ButtonRelease-1>", select_history)

# Button Layout
buttons = [
    ["C", "⌫", "()", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

# Button Frame
button_frame = tk.Frame(root, bg="black")
button_frame.pack()

def make_button(text, row, col):
    bg_color = "#1E1E1E"
    if text == "=":
        bg_color = "#A066D3"
    elif text == "C":
        bg_color = "#444444"

    tk.Button(button_frame,
              text=text,
              font=("Helvetica", 16),
              bg=bg_color,
              fg="white",
              activebackground=bg_color,
              activeforeground="white",
              width=3,
              height=2,
              relief="flat",
              bd=0,
              command=lambda: click(text)
              ).grid(row=row, column=col, padx=6, pady=6, ipadx=1, ipady=8)

# Create Buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        make_button(char, r, c)

root.mainloop()