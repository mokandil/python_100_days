import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.minsize(600, 400)
        self.master.title("Simple GUI App")

        # create label
        self.label = tk.Label(master, text="Enter your name:")
        self.label.pack()

        # create entry field
        self.entry = tk.Entry(master)
        self.entry.pack()

        # create button
        self.button = tk.Button(master, text="Click me!", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        name = self.entry.get()
        message = f"Hello, {name}!"
        self.label.config(text=message)


# create app
window = tk.Tk()
app = App(window)

# start app
window.mainloop()
