import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Virtual Dice Roller")

# Create a button to roll the dice
roll_button = tk.Button(window, text="Roll the Dice", command=roll_dice)
roll_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 24))
result_label.pack()

# Run the main event loop
window.mainloop()
