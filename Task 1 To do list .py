import tkinter as tk
from datetime import datetime

tasks = []

root = tk.Tk()
root.title("To-Do List")

tk.Label(root, text="Welcome to New To-Do List", font=("Helvetica", 14, "bold")).pack(pady=10)

home_frame = tk.Frame(root, bg="#e5ccff")
add_frame = tk.Frame(root, bg="#ffffff")
view_frame = tk.Frame(root, bg="#ffffcc")

def show_frame(frame):
    for f in (home_frame, add_frame, view_frame):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

def add_task():
    task = entry_task.get()
    time = entry_time.get()
    if task:
        today = datetime.now().strftime("%A")
        tasks.append({"task": task, "time": time, "day": today, "done": False})
        entry_task.delete(0, tk.END)
        entry_time.delete(0, tk.END)
        show_frame(home_frame)

def refresh_tasks():
    listbox.delete(0, tk.END)
    congrats_label.pack_forget()

    if not tasks:
        listbox.insert(tk.END, "No tasks yet.")
    elif all(t["done"] for t in tasks):
        congrats_label.pack(pady=10)
    else:
        for t in tasks:
            mark = "✓" if t["done"] else " "
            listbox.insert(tk.END, f"[{mark}] {t['task']} at {t['time']} on {t['day']}")

def mark_done():
    sel = listbox.curselection()
    if sel:
        tasks[sel[0]]["done"] = True
        refresh_tasks()

def remove_all():
    tasks.clear()
    refresh_tasks()

# Dashboard / Home Frame
tk.Button(home_frame, text="Add Task", command=lambda: show_frame(add_frame)).pack(pady=10)
tk.Button(home_frame, text="Checklist", command=lambda: [refresh_tasks(), show_frame(view_frame)]).pack(pady=10)
tk.Button(home_frame, text="Remove All", command=remove_all).pack(pady=10)

# Add Frame
entry_task = tk.Entry(add_frame, width=30)
entry_task.pack(pady=5)
entry_time = tk.Entry(add_frame, width=30)
entry_time.insert(0, "Time (e.g. 5 PM)")
entry_time.pack(pady=5)
tk.Button(add_frame, text="Submit", command=add_task).pack()
tk.Button(add_frame, text="Back", command=lambda: show_frame(home_frame)).pack(pady=5)

# View Frame
listbox = tk.Listbox(view_frame, width=40, height=10, bg="yellow", fg="black", font=("Helvetica", 10))
listbox.pack(pady=5)
congrats_label = tk.Label(view_frame, text="Congratulations! All tasks are completed.", bg="green", fg="white")
tk.Button(view_frame, text="Mark Done", command=mark_done).pack()
tk.Button(view_frame, text="Back", command=lambda: show_frame(home_frame)).pack(pady=5)

# Start with home screen
show_frame(home_frame)
root.mainloop()