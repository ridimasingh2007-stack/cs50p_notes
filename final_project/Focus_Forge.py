import tkinter as tk
from tkinter import messagebox
import random
import json

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def is_valid_time(value):
    return value.isdigit() and int(value) > 0

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FocusForge 🍅")
        self.root.geometry("600x650")

        self.running = False
        self.time_left = 0
        self.sessions_completed = 0

        self.messages = [
            "Amazing work! Keep the momentum going 🚀",
            "Small progress is still progress 🌟",
            "You're one step closer to your goal 🎯",
            "Consistency beats motivation 🔥",
            "Future you will thank you for this session 😎"
        ]

        # Title
        tk.Label(
            root,
            text="FocusForge 🍅",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        # Settings Frame
        settings = tk.Frame(root)
        settings.pack(pady=10)

        tk.Label(settings, text="Focus Time (min)").grid(row=0, column=0)
        self.focus_entry = tk.Entry(settings, width=10)
        self.focus_entry.insert(0, "25")
        self.focus_entry.grid(row=0, column=1)

        tk.Label(settings, text="Break Time (min)").grid(row=1, column=0)
        self.break_entry = tk.Entry(settings, width=10)
        self.break_entry.insert(0, "5")
        self.break_entry.grid(row=1, column=1)

        tk.Label(settings, text="Daily Goal").grid(row=2, column=0)
        self.goal_entry = tk.Entry(settings, width=10)
        self.goal_entry.insert(0, "6")
        self.goal_entry.grid(row=2, column=1)

        # Timer
        self.timer_label = tk.Label(
            root,
            text="25:00",
            font=("Arial", 40)
        )
        self.timer_label.pack(pady=20)

        # Session Counter
        self.session_label = tk.Label(
            root,
            text="Sessions Completed: 0"
        )
        self.session_label.pack()

        # Tasks Section
        tk.Label(
            root,
            text="Tasks",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack()

        self.add_task_btn = tk.Button(
            root,
            text="Add Task",
            command=self.add_task
        )
        self.add_task_btn.pack(pady=5)

        self.complete_task_btn = tk.Button(
        root,
        text="Mark Complete",
        command=self.complete_task
        )
        self.complete_task_btn.pack()

        self.task_list = tk.Listbox(root, width=50, height=10)
        self.task_list.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Start",
            command=self.start_timer
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="Pause",
            command=self.pause_timer
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_timer
        ).grid(row=0, column=2, padx=10)

        self.load_data()


    def add_task(self):
        task = self.task_entry.get().strip()

        if task:
            self.task_list.insert(
                tk.END, f"☐ {task}")
            self.task_entry.delete(0, tk.END)
            self.save_data()
            

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1

            self.timer_label.config(
                text=format_time(self.time_left)
            )

            self.root.after(1000, self.update_timer)

        elif self.time_left == 0 and self.running:
            self.running = False

            self.sessions_completed += 1
            self.save_data()
            self.session_label.config(
                text=f"Sessions Completed: {self.sessions_completed}"
            )

            messagebox.showinfo(
                "Session Complete!",
                random.choice(self.messages)
            )

    def start_timer(self):
        if not self.running:
            try:
                focus_time = int(self.focus_entry.get())
                self.time_left = focus_time * 60
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Enter valid numbers."
                )
                return

            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False

        try:
            focus_time = int(self.focus_entry.get())
            self.time_left = focus_time * 60
        except ValueError:
            self.time_left = 1500

        self.timer_label.config(
            text=format_time(self.time_left)
        )

    def save_data(self):
        data = {
            "tasks": list(self.task_list.get(0, tk.END)),
            "sessions_completed": self.sessions_completed,
            "focus_time": self.focus_entry.get(),
            "break_time": self.break_entry.get(),
            "daily_goal": self.goal_entry.get()
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            self.sessions_completed = data["sessions_completed"]

            self.session_label.config(
                text=f"Sessions Completed: {self.sessions_completed}"
            )

            self.focus_entry.delete(0, tk.END)
            self.focus_entry.insert(0, data["focus_time"])

            self.break_entry.delete(0, tk.END)
            self.break_entry.insert(0, data["break_time"])

            self.goal_entry.delete(0, tk.END)
            self.goal_entry.insert(0, data["daily_goal"])

            for task in data["tasks"]:
                self.task_list.insert(tk.END, task)

        except FileNotFoundError:
            pass
    def complete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "No Task Selected",
                "Please select a task first."
            )
            return

        index = selected[0]

        task = self.task_list.get(index)

        if not task.startswith("☑"):
            task = task.replace("☐", "☑", 1)

            self.task_list.delete(index)
            self.task_list.insert(index, task)

            self.save_data()
def main():
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

    
