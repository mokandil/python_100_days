import tkinter as tk

# Create the main window
window = tk.Tk()
# Set the title of the window
window.title("My First GUI Program")
# Set the size of the window
window.minsize(width=500, height=300)

# create a function to handle button clicks
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    label.config(text=new_text)


# Create a label
label = tk.Label(window, text="Hello World", font=("Arial", 24, "bold"))
label.pack()  # Add the label to the window

# Create a button
button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()  # Add the button to the window


# create input field
input = tk.Entry(window, width=20)
input.pack()





# Start the main event loop
window.mainloop()