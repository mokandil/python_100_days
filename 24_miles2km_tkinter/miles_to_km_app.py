""" Miles to Km Converter App
  +------------------------------------+
  |                                    |
  |     Enter =>  [    ] Miles         |
  |                                    |
  |  is equivalent to  [         ] Km  |
  |                                    |
  |              [ Calculate ]         |
  |                                    |
  +------------------------------------+

"""

import tkinter as tk

FONT = ("Arial", 10)


class MilesToKmConverter:
    def __init__(self):
        # create window
        self.window = tk.Tk()
        self.window.title("Miles to Km Converter")
        self.window.minsize(width=300, height=200)
        self.window.config(padx=50, pady=50)

        # create label widget to display text
        self.input_label = tk.Label(text="Enter Miles:", font=FONT)
        self.input_label.config(padx=10, pady=10)

        # create entry widget to accept user input
        self.input_entry = tk.Entry(width=10, font=FONT)

        # create label widget to display "Miles" text
        self.miles_label = tk.Label(text="Miles", font=FONT)
        self.miles_label.config(padx=10, pady=10)
        
        # create label widget to display "is equivalent to"
        self.output_label = tk.Label(text="is equivalent to", font=FONT)
        self.output_label.config(padx=10, pady=10)
        
        # create label widget to display output
        self.output_value_label = tk.Label(text="", font=FONT)
        
        # create label widget to display "Km" text
        self.km_label = tk.Label(text="Km", font=FONT)
        # self.km_label.config(padx=10, pady=10)
        
        # create button widget to trigger conversion
        self.calculate_button = tk.Button(text="Calculate", font=FONT, command=self.calculate_km)
        

        # placing widgets on the screen
        self.input_label.grid(column=0, row=0)
        self.input_entry.grid(column=1, row=0)
        self.miles_label.grid(column=2, row=0)
        self.output_label.grid(column=0, row=1)
        self.output_value_label.grid(column=1, row=1)
        self.km_label.grid(column=2, row=1)
        self.calculate_button.grid(column=1, row=2)
        
        self.window.mainloop()

    # conversion logic
    def calculate_km(self):
        miles = float(self.input_entry.get())
        km = miles * 1.609
        self.output_value_label.config(text=f"{round(km, 2)}")


if __name__ == "__main__":
    converter = MilesToKmConverter()
