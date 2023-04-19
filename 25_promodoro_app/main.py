import tkinter as tk
import time
import os
from PIL import Image, ImageTk

# get the name of the current directory
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "promodoro.jpg")

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.minsize(300, 300)
        self.master.config(padx=50, pady=50)
        master.title("Pomodoro Timer")
        master.resizable(False, False)

        self.current_status = "Work"
        self.sessions_completed = 0
        self.minutes = 25
        self.seconds = 0
        self.timer_running = False

        # Create canvas widget and add background image
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        # loading the image and resizing it
        # self.image = Image.open(image_path)
        # self.image = self.image.resize((300, 300))
        # self.image = ImageTk.PhotoImage(self.image)
        # self.canvas.create_image(0, 0, anchor="nw", image=self.image)


        # Create widgets
        self.status_label = tk.Label(self.canvas, text=self.current_status, font=("Arial", 24))
        self.session_label = tk.Label(self.canvas, text="Sessions completed: " + str(self.sessions_completed), font=("Arial", 12))
        self.time_label = tk.Label(self.canvas, text="25:00", font=("Arial", 48))

        self.start_button = tk.Button(self.canvas, text="Start", command=self.start_timer)
        self.pause_button = tk.Button(self.canvas, text="Pause", command=self.pause_timer, state="disabled")
        self.reset_button = tk.Button(self.canvas, text="Reset", command=self.reset_timer, state="disabled")
        self.stop_button = tk.Button(self.canvas, text="Stop", command=self.stop_timer, state="disabled")

        # Place widgets on canvas
        self.canvas.create_window(150, 50, window=self.status_label)
        self.canvas.create_window(150, 100, window=self.session_label)
        self.canvas.create_window(150, 180, window=self.time_label)
        self.canvas.create_window(75, 250, window=self.start_button)
        self.canvas.create_window(225, 250, window=self.pause_button)
        self.canvas.create_window(75, 280, window=self.reset_button)
        self.canvas.create_window(225, 280, window=self.stop_button)

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.stop_button.config(state="normal")
        self.update_timer()

    def pause_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")

    def reset_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.stop_button.config(state="disabled")
        self.minutes = 25
        self.seconds = 0
        self.update_time_label()

    def stop_timer(self):
        if self.current_status == "Work":
            self.sessions_completed += 1
            if self.sessions_completed % 4 == 0:
                self.current_status = "Long Break"
                self.minutes = 15
            else:
                self.current_status = "Short Break"
                self.minutes = 5
        else:
            self.current_status = "Work"
            self.minutes = 25
        self.seconds = 0

        # reset the number of sessions completed if the user has completed 4 sessions
        if self.sessions_completed % 4 == 0:
            self.sessions_completed = 0
            
        self.session_label.config(text="Sessions completed: " + str(self.sessions_completed))
        self.status_label.config(text=self.current_status)
        self.update_time_label()

    def update_timer(self):
        if self.timer_running:
            if self.minutes == 0 and self.seconds == 0:
                self.stop_timer()
            elif self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1
            self.update_time_label()
            self.master.after(1000, self.update_timer)

    def update_time_label(self):
        self.time_label.config(text="{:02d}:{:02d}".format(self.minutes, self.seconds))

# Create the main window
root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()
